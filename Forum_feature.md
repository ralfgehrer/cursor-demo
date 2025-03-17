# Feature Implementation Plan: Forum System

## 1. Overview
Feature Description: Add a forum-like feature to the application with a dedicated page accessible from the sidebar navigation. Users will be able to create discussions, reply to threads, and view all forum posts.

## 2. Requirements
- **Functional Requirements:**
  - View list of forum threads
  - Create new discussion threads
  - Reply to existing threads
  - Sort/filter discussions
  - Pagination support
  - Thread categories/tags

- **Non-functional Requirements:**
  - Responsive design matching existing UI
  - Real-time updates for new posts
  - Efficient loading of thread lists

- **Dependencies:**
  - Backend API endpoints for forum CRUD operations
  - @chakra-ui/react (existing)
  - @tanstack/react-query (existing)
  - @tanstack/react-router (existing)

## 3. Implementation Steps

### Step 1: Add Forum Navigation Item
**Objective:** Add forum link to sidebar navigation
**File Changes:**
```typescript:frontend/src/components/Common/SidebarItems.tsx
// Add forum icon import
import { FiMessageSquare } from "react-icons/fi"

const items = [
  { icon: FiHome, title: "Dashboard", path: "/" },
  { icon: FiBriefcase, title: "Items", path: "/items" },
  { icon: FiMessageSquare, title: "Forum", path: "/forum" }, // Add this
  { icon: FiSettings, title: "User Settings", path: "/settings" },
]
```

### Step 2: Create Forum Route
**Objective:** Set up forum route and base component
**File Changes:**
```typescript:frontend/src/routes/_layout/forum.tsx
import { Container, Heading } from "@chakra-ui/react"
import { createFileRoute } from "@tanstack/react-router"
import { z } from "zod"

const forumSearchSchema = z.object({
  page: z.number().catch(1),
  category: z.string().optional(),
  sort: z.enum(['latest', 'popular']).catch('latest'),
})

export const Route = createFileRoute("/_layout/forum")({
  component: Forum,
  validateSearch: (search) => forumSearchSchema.parse(search),
})

function Forum() {
  return (
    <Container maxW="full">
      <Heading size="lg" textAlign={{ base: "center", md: "left" }} pt={12}>
        Forum Discussions
      </Heading>
      {/* Forum content will go here */}
    </Container>
  )
}
```

### Step 3: Create Forum Components
**Objective:** Build core forum UI components
**New Files:**
```typescript:frontend/src/components/Forum/ThreadList.tsx
// Thread list component with pagination
```

```typescript:frontend/src/components/Forum/CreateThread.tsx
// New thread modal component 
```

# Step 3 Detailed Breakdown: Forum Components Implementation

## 3.1 Thread List Component
**Objective:** Create main forum view showing all threads with filtering and pagination
**File:** `frontend/src/components/Forum/ThreadList.tsx`
```typescript:frontend/src/components/Forum/ThreadList.tsx
interface Thread {
  id: string
  title: string
  content: string
  author: UserPublic
  created_at: string
  replies_count: number
  last_activity: string
  category: string
}

interface ThreadListProps {
  threads: Thread[]
  isLoading: boolean
  onThreadClick: (id: string) => void
}

const ThreadList = ({ threads, isLoading }: ThreadListProps) => {
  return (
    <VStack spacing={4} w="full">
      {threads.map(thread => (
        <ThreadCard key={thread.id} thread={thread} />
      ))}
      {/* Pagination component here */}
    </VStack>
  )
}
```

## 3.2 Thread Card Component
**Objective:** Individual thread preview card in the list
**File:** `frontend/src/components/Forum/ThreadCard.tsx`
```typescript:frontend/src/components/Forum/ThreadCard.tsx
const ThreadCard = ({ thread }: { thread: Thread }) => {
  return (
    <Box 
      p={4} 
      borderWidth="1px" 
      borderRadius="lg"
      _hover={{ bg: 'gray.50' }}
    >
      <Flex justify="space-between">
        <VStack align="start">
          <Heading size="md">{thread.title}</Heading>
          <Text noOfLines={2}>{thread.content}</Text>
        </VStack>
        <ThreadStats replies={thread.replies_count} />
      </Flex>
      <ThreadFooter author={thread.author} date={thread.created_at} />
    </Box>
  )
}
```

## 3.3 Create Thread Modal
**Objective:** Modal for creating new threads
**File:** `frontend/src/components/Forum/CreateThread.tsx`
```typescript:frontend/src/components/Forum/CreateThread.tsx
interface CreateThreadProps {
  isOpen: boolean
  onClose: () => void
}

const CreateThread = ({ isOpen, onClose }: CreateThreadProps) => {
  const form = useForm<{
    title: string
    content: string
    category: string
  }>()
  
  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <ModalOverlay />
      <ModalContent>
        <form onSubmit={form.handleSubmit(onSubmit)}>
          {/* Form fields */}
        </form>
      </ModalContent>
    </Modal>
  )
}
```

## 3.4 Thread View Component
**Objective:** Full thread view with replies
**File:** `frontend/src/components/Forum/ThreadView.tsx`
```typescript:frontend/src/components/Forum/ThreadView.tsx
interface ThreadViewProps {
  threadId: string
}

const ThreadView = ({ threadId }: ThreadViewProps) => {
  const { data: thread } = useQuery({
    queryKey: ['thread', threadId],
    queryFn: () => ForumService.getThread(threadId)
  })
  
  return (
    <VStack spacing={6} align="stretch">
      <ThreadHeader thread={thread} />
      <ReplyList replies={thread.replies} />
      <AddReply threadId={threadId} />
    </VStack>
  )
}
```

## 3.5 Required API Types
**File:** `frontend/src/client/models.ts`
```typescript:frontend/src/client/models.ts
export interface Thread {
  id: string
  title: string
  content: string
  author_id: string
  created_at: string
  updated_at: string
  category: string
  replies_count: number
}

export interface ThreadReply {
  id: string
  thread_id: string
  content: string
  author_id: string
  created_at: string
}

export interface ThreadsResponse {
  data: Thread[]
  count: number
}
```

## 3.6 Forum Service Integration
**File:** `frontend/src/client/services/forum.ts`
```typescript:frontend/src/client/services/forum.ts
export const ForumService = {
  getThreads: async (params: {
    limit?: number
    skip?: number
    category?: string
  }): Promise<ThreadsResponse> => {
    return api.get('/forum/threads', { params })
  },
  
  createThread: async (data: {
    title: string
    content: string
    category: string
  }): Promise<Thread> => {
    return api.post('/forum/threads', data)
  },
  
  // Additional methods for replies, etc.
}
```

## Required Changes to Existing Files:

1. Update route configuration:
```typescript:frontend/src/routeTree.gen.ts
// Add forum routes to FileRoutesByPath interface
'/_layout/forum': {
  preLoaderRoute: typeof ForumImport
  parentRoute: typeof LayoutImport
}
```

2. Add Navbar integration:
```typescript:frontend/src/routes/_layout/forum.tsx
function Forum() {
  return (
    <Container maxW="full">
      <Heading size="lg" textAlign={{ base: "center", md: "left" }} pt={12}>
        Forum Discussions
      </Heading>
      <Navbar 
        type="Thread" 
        addModalAs={CreateThread}
      />
      <ThreadList />
    </Container>
  )
}
```

## Dependencies to Install:
- None additional - using existing Chakra UI components and React Query

Would you like me to expand on any of these components or move on to implementing a specific part?

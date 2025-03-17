const ITEM_TEMPLATES = [
  {
    title: "Project Planning Document",
    description: "Comprehensive project planning document outlining objectives, timelines, and deliverables"
  },
  {
    title: "User Research Report",
    description: "Detailed findings from user interviews and usability testing sessions"
  },
  {
    title: "Design System Guidelines",
    description: "Complete design system documentation including color palette, typography, and component library"
  },
  {
    title: "API Integration Spec",
    description: "Technical specification for third-party API integration with authentication flow"
  },
  {
    title: "Performance Optimization Plan",
    description: "Strategy document for improving application performance and load times"
  },
  {
    title: "Security Audit Report",
    description: "Security assessment findings and recommended improvements"
  },
  {
    title: "Content Strategy Document",
    description: "Content planning and governance guidelines for the platform"
  },
  {
    title: "Deployment Checklist",
    description: "Pre-deployment verification steps and post-deployment monitoring plan"
  }
]

export const getMockItemData = () => {
  const randomIndex = Math.floor(Math.random() * ITEM_TEMPLATES.length)
  return ITEM_TEMPLATES[randomIndex]
} 
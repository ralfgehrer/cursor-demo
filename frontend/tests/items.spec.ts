import { test, expect } from '@playwright/test';
import { firstSuperuser, firstSuperuserPassword } from "./config";
import { logInUser } from "./utils/user";

test.describe('Items Management Screen', () => {
  // Ensure clean state for each test
  test.use({ storageState: { cookies: [], origins: [] } });

  test('should display items page after login', async ({ page }) => {
    // Sign in first
    await logInUser(page, firstSuperuser, firstSuperuserPassword);
    
    // Navigate to items page
    await page.goto('/items');
    
    // Basic check - just verify the heading is visible
    await expect(page.getByRole('heading', { name: 'Items Management' })).toBeVisible();
  });
});
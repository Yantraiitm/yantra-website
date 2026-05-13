# Yantra Website Frontend - Vue 3 + Vite

A modern, fast, and fully refactored Vue 3 + Vite application for the Yantra Robotics Society website.

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ installed
- npm or yarn package manager

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

The development server will run on `http://localhost:5173`

## 📁 Project Structure

```
src/
├── components/          # Reusable Vue components
│   ├── Preloader.vue    # Loading animation
│   ├── Navbar.vue       # Navigation bar
│   └── Footer.vue       # Footer
├── pages/               # Page components (routed)
│   ├── Home.vue
│   ├── About.vue
│   ├── Team.vue
│   ├── Projects.vue
│   ├── Courses.vue
│   ├── Events.vue
│   ├── Gallery.vue
│   ├── Blog.vue
│   ├── Contact.vue
│   ├── Join.vue
│   └── NotFound.vue
├── services/            # API and external services
│   ├── api.js           # Axios HTTP client
│   └── supabase.js      # Supabase SDK setup
├── stores/              # Pinia state management
│   ├── user.js          # User authentication store
│   └── blog.js          # Blog posts store
├── styles/              # Global styles
│   └── style.css        # Main stylesheet (preserved from original)
├── App.vue              # Root component
├── main.js              # Entry point
└── router.js            # Vue Router configuration
```

## 🎨 Styling

All original CSS styling has been preserved and migrated to `src/styles/style.css`. The design maintains:
- **Industrial Amber Theme** with warm color palette
- **Responsive Design** for all screen sizes
- **Performance-first** optimized CSS

### CSS Variables (available in all components)
```css
--bg-primary: #0E0E0E
--amber: #F59E0B
--rust: #EA580C
--text-primary: #F5F0E8
--border: rgba(245,158,11,0.12)
/* ...and more */
```

## 🔧 Configuration

### Environment Variables

Create a `.env.local` file:

```env
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_public_key
VITE_API_URL=http://localhost:5000
VITE_ENVIRONMENT=development
```

## 📚 Available Scripts

```bash
# Development
npm run dev              # Start dev server

# Production
npm run build           # Build for production
npm run preview         # Preview production build

# Code Quality
npm run lint            # Run ESLint
```

## 🛣️ Routing

The website uses Vue Router with the following routes:
- `/` - Home
- `/about` - About
- `/team` - Team members
- `/projects` - Projects showcase
- `/courses` - Courses and workshops
- `/events` - Upcoming events
- `/gallery` - Photo gallery
- `/blog` - Blog posts
- `/contact` - Contact form
- `/join` - Join application
- `/:pathMatch(.)*` - 404 Not Found

## 🔌 API Integration

The frontend communicates with the backend via axios client with automatic:
- Base URL routing (`/api` prefix)
- JWT token injection from localStorage
- Error handling and auth redirects

### Example API calls:
```javascript
// In components or stores
import apiClient from '@/services/api'

// GET
const { data } = await apiClient.get('/blog')

// POST
const { data } = await apiClient.post('/contact', formData)

// PUT
await apiClient.put(`/blog/${id}`, updateData)

// DELETE
await apiClient.delete(`/blog/${id}`)
```

## 🔐 Authentication

Uses Supabase Auth with JWT tokens:
```javascript
import { authService } from '@/services/supabase'

// Sign up
await authService.signUp(email, password)

// Sign in
const session = await authService.signIn(email, password)

// Get current user
const user = await authService.getCurrentUser()

// Sign out
await authService.signOut()
```

## 📦 Dependencies

- **Vue 3** - Progressive JavaScript framework
- **Vite** - Next generation build tool
- **Vue Router** - Official router for Vue
- **Pinia** - Vue state management
- **Axios** - HTTP client
- **Supabase** - Backend & database

## 🎯 Features

✅ **100% CSS Preserved** - Original styling maintained  
✅ **Component-based** - Reusable Vue components  
✅ **Type-ready** - Can add TypeScript support  
✅ **Fast HMR** - Hot Module Reloading in dev  
✅ **State Management** - Pinia stores for app state  
✅ **API Ready** - Pre-configured Axios client  
✅ **Responsive** - Mobile-first design  
✅ **Dark Theme** - Industrial amber color scheme  

## 🚀 Deployment

### Vercel (Recommended)
```bash
# Push to GitHub, Vercel auto-deploys
npm run build
```

Environment variables in Vercel dashboard:
- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`
- `VITE_API_URL`

### Netlify
```bash
npm run build
# Deploy dist folder
```

## 📖 Development Tips

### Adding a new page
1. Create `src/pages/MyPage.vue`
2. Add route in `src/router.js`
3. Add navigation link in `Navbar.vue`

### Creating a component
1. Create `src/components/MyComponent.vue`
2. Import and use in pages or other components
3. Use Pinia stores for shared state

### Adding an API call
1. Use `apiClient` from `src/services/api.js`
2. Handle loading/error states with ref
3. Consider adding to Pinia stores for shared data

## 🐛 Troubleshooting

**Port 5173 already in use**
```bash
npm run dev -- --port 3000
```

**Module not found errors**
```bash
rm -rf node_modules package-lock.json
npm install
```

**Styling not applying**
- Ensure `src/styles/style.css` is imported in `main.js`
- CSS variables must be available in `:root` scope

## 📞 Support

For issues or questions:
- GitHub: https://github.com/yantra
- Email: contact@yantra.iitmbs.ac.in
- Instagram: @yantra_iitm

## 📄 License

This project is part of Yantra Robotics Society, IIT Madras BS.

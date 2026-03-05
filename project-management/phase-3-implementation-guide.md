# Phase 3: Frontend Dashboard - Implementation Guide

## Objectives
Build a responsive, user-friendly dashboard frontend using Next.js and React that integrates with the backend API.

## Deliverables

### 1. Authentication UI (`frontend/pages/auth/`)
- [x] Login page with email/password form
- [x] Registration page with user details
- [ ] Logout functionality
- [ ] Password reset flow
- [ ] Session management

**Files to Create**:
- `frontend/pages/auth/login.js` - Login page
- `frontend/pages/auth/register.js` - Registration page
- `frontend/components/AuthForm.js` - Reusable auth form
- `frontend/hooks/useAuth.js` - Authentication hook

### 2. Main Dashboard (`frontend/pages/dashboard/`)
- [x] Overview with key metrics (4 cards)
- [ ] Recent orders list
- [ ] Top vendors list
- [ ] Opportunities alerts
- [ ] Real-time notifications

**Files to Create**:
- `frontend/pages/dashboard/index.js` - Main dashboard
- `frontend/components/MetricsCard.js` - Metric cards
- `frontend/components/RecentOrders.js` - Orders widget
- `frontend/components/TopVendors.js` - Vendors widget

### 3. Vendor Management UI (`frontend/pages/vendors/`)
- [ ] Vendor list with filters
- [ ] Vendor detail page
- [ ] Create vendor form
- [ ] Edit vendor form
- [ ] Vendor verification workflow
- [ ] Fraud score display

**Files to Create**:
- `frontend/pages/vendors/index.js` - Vendors list
- `frontend/pages/vendors/[id].js` - Vendor details
- `frontend/pages/vendors/new.js` - Create vendor
- `frontend/components/VendorForm.js` - Vendor form
- `frontend/components/VendorTable.js` - Vendors table

### 4. Order Management UI (`frontend/pages/orders/`)
- [ ] Orders list with status
- [ ] Create new order
- [ ] Order details page
- [ ] Send RFQ action
- [ ] Order status tracking

**Files to Create**:
- `frontend/pages/orders/index.js` - Orders list
- `frontend/pages/orders/[id].js` - Order details
- `frontend/pages/orders/new.js` - Create order
- `frontend/components/OrderForm.js` - Order form
- `frontend/components/OrderStatus.js` - Status display

### 5. Quote Management UI (`frontend/pages/quotes/`)
- [ ] Quote comparison interface
- [ ] Quote list by order
- [ ] Best deal recommendation
- [ ] Quote details
- [ ] Quick accept/reject

**Files to Create**:
- `frontend/pages/quotes/index.js` - Quotes list
- `frontend/pages/quotes/compare.js` - Comparison view
- `frontend/components/QuoteTable.js` - Quotes table
- `frontend/components/QuoteComparison.js` - Comparison widget

### 6. Analytics Dashboard (`frontend/pages/analytics/`)
- [ ] Vendor performance metrics
- [ ] Deal success trends
- [ ] Price analytics
- [ ] Lead conversion metrics
- [ ] Charts and visualizations

**Files to Create**:
- `frontend/pages/analytics/index.js` - Analytics dashboard
- `frontend/components/VendorAnalytics.js` - Vendor metrics
- `frontend/components/DealAnalytics.js` - Deal metrics
- `frontend/components/PriceChart.js` - Price trends
- `frontend/components/LeadMetrics.js` - Lead funnel

### 7. Common Components
- [ ] Navigation header
- [ ] Sidebar menu
- [ ] Footer
- [ ] Search components
- [ ] Form fields
- [ ] Tables and pagination
- [ ] Modals and dialogs
- [ ] Loading states
- [ ] Error messages

**Files to Create**:
- `frontend/components/Header.js` - Top navigation
- `frontend/components/Sidebar.js` - Side navigation
- `frontend/components/Footer.js` - Footer
- `frontend/components/Layout.js` - Main layout
- `frontend/components/SearchBar.js` - Search component
- `frontend/components/Table.js` - Reusable table
- `frontend/components/Modal.js` - Modal dialog
- `frontend/components/Button.js` - Button component
- `frontend/components/Badge.js` - Status badges

### 8. API Integration
- [ ] API client setup
- [ ] Authentication context
- [ ] API hooks for each resource
- [ ] Error handling
- [ ] Loading states

**Files to Create**:
- `frontend/lib/api.js` - API client
- `frontend/lib/auth.js` - Authentication utilities
- `frontend/hooks/useAPI.js` - Generic API hook
- `frontend/hooks/useVendors.js` - Vendors hook
- `frontend/hooks/useOrders.js` - Orders hook
- `frontend/hooks/useQuotes.js` - Quotes hook
- `frontend/hooks/useAnalytics.js` - Analytics hook
- `frontend/context/AuthContext.js` - Auth context

### 9. Styling and Responsive Design
- [x] TailwindCSS configuration
- [ ] Custom theme colors
- [ ] Dark mode support
- [ ] Mobile responsive layouts
- [ ] Accessibility (WCAG)

**Files to Create**:
- `frontend/styles/theme.css` - Custom theme
- `frontend/tailwind.config.js` - Tailwind config
- Media queries for responsive design

### 10. State Management
- [ ] Context API setup
- [ ] Global state for auth
- [ ] Sidebar menu state
- [ ] Form state management
- [ ] Caching strategy

**Files to Create**:
- `frontend/context/GlobalContext.js` - Global state
- `frontend/context/StorageContext.js` - Local storage

## Technical Stack
- Next.js 14.0.4
- React 18
- TailwindCSS 3.3.6
- Axios (API calls)
- React Query (optional - data caching)

## Implementation Steps

### Week 1: Foundation
1. Set up Next.js project structure
2. Create layout components (Header, Sidebar, Footer)
3. Implement authentication pages
4. Set up API client and auth context
5. Create reusable UI components

### Week 2: Core Features
1. Implement dashboard page
2. Create vendor management UI
3. Build order management interface
4. Develop quote comparison view
5. API integration for all features

### Week 3: Polish
1. Add analytics dashboard
2. Implement advanced filters
3. Add charts and visualizations
4. Mobile responsive design
5. Performance optimization
6. Testing and bug fixes

## API Integration Points

### Authentication
```javascript
POST /api/v1/auth/register
POST /api/v1/auth/login
GET /api/v1/auth/profile
```

### Vendors
```javascript
GET /api/v1/vendors?city=&category=&verification_status=
POST /api/v1/vendors
GET /api/v1/vendors/{id}
PUT /api/v1/vendors/{id}
DELETE /api/v1/vendors/{id}
POST /api/v1/vendors/{id}/verify
POST /api/v1/vendors/{id}/flag
```

### Orders
```javascript
GET /api/v1/orders
POST /api/v1/orders
GET /api/v1/orders/{id}
PUT /api/v1/orders/{id}
DELETE /api/v1/orders/{id}
POST /api/v1/orders/{id}/send-rfq
```

### Quotes
```javascript
GET /api/v1/quotes
POST /api/v1/quotes
PUT /api/v1/quotes/{id}
```

### Analytics
```javascript
GET /api/v1/analytics/vendors
GET /api/v1/analytics/deals
GET /api/v1/analytics/prices
GET /api/v1/analytics/leads
```

## Success Criteria

- [ ] All pages load and display correctly
- [ ] User can login and access dashboard
- [ ] CRUD operations work for all resources
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] API calls are successful
- [ ] Loading states show during API calls
- [ ] Error messages display on failures
- [ ] Form validation works
- [ ] Navigation between pages works
- [ ] Data refreshes on updates

## Live Demo
When completed, the frontend will be accessible at:
- **Development**: `http://localhost:3000`
- **Production**: To be configured

## Notes

1. **API Base URL**: Configure in `frontend/lib/api.js` to point to backend (default: `http://localhost:8000/api/v1`)
2. **Authentication**: JWT token stored in localStorage
3. **Error Handling**: Global error boundary component needed
4. **Loading**: Skeleton loaders for better UX
5. **Caching**: Consider React Query for automatic cache management
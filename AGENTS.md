# AGENTS.md

## Project Overview

This is a static website for **Maison Remodeling Group**, a residential remodeling and renovation company based in San Jose, CA. The website showcases their services, project portfolio, blog content, and serves as a lead generation platform.

---

## Tech Stack

| Technology | Purpose | Source |
|------------|---------|--------|
| HTML5 | Static pages | N/A |
| Tailwind CSS | Utility-first styling | CDN: `cdn.tailwindcss.com` |
| Vanilla JavaScript | Interactivity | Embedded in HTML |
| Three.js | Hero section particle animation | CDN: `cdnjs.cloudflare.com` |
| GSAP + ScrollTrigger | Scroll animations, parallax | CDN: `cdnjs.cloudflare.com` |
| Lucide Icons | Icon library | CDN: `unpkg.com/lucide@latest` |
| Google Fonts | Typography | Playfair Display (headings), Inter (body) |

---

## Project Structure

```
website-for-client/
├── assets/                          # All images, logos, icons (~100 files)
│   ├── new_logo.png                 # Primary company logo
│   ├── favicon.png                  # Site favicon
│   ├── kitchen-*.jpg                # Kitchen project images
│   ├── bathroom-*.jpg               # Bathroom project images
│   ├── home-*.jpg                   # Home remodeling images
│   ├── adu-*.jpg                    # ADU project images
│   ├── exterior-*.jpg               # Exterior project images
│   ├── commercial-*.jpg             # Commercial project images
│   ├── hero-*.jpg                   # Hero section backgrounds
│   ├── blog-*.jpg                   # Blog article images
│   ├── team-*.jpg                   # Team member photos
│   └── [partner-logos].*            # Vendor/partner logos (cabinets, tiles, etc.)
│
├── blog/                            # Blog article pages (6 articles)
│   ├── adu-building-guide.html
│   ├── bathroom-design-ideas.html
│   ├── home-addition-ideas.html
│   ├── home-remodeling-guide-2025.html
│   ├── kitchen-cabinets-guide.html
│   └── kitchen-remodeling-trends-2025.html
│
├── projects/                        # Project gallery pages (5 galleries)
│   ├── bathroom-remodeling.html
│   ├── complete-home-remodeling.html
│   ├── condo-remodeling.html
│   ├── kitchen-remodeling.html
│   └── outdoor-remodeling.html
│
├── index.html                       # Homepage (hero, services, testimonials)
├── about.html                       # Company about page
├── contact.html                     # Contact form + business info
├── blog.html                        # Blog index page
├── projects.html                    # Projects index page
├── testimonials.html                # Customer testimonials page
├── products.html                    # Product partners page
├── locations.html                   # Service areas page
├── privacy-policy.html              # Privacy policy
├── terms-of-use.html                # Terms of use
│
├── [service-pages].html             # Individual service pages:
│   ├── kitchen-remodeling.html
│   ├── bathroom-remodeling.html
│   ├── home-remodeling.html
│   ├── home-additions.html
│   ├── adu.html
│   ├── exterior-remodeling.html
│   ├── custom-homes.html
│   ├── commercial-remodeling.html
│   └── design-build.html
│
├── llm.txt                          # LLM context file with business info
└── AGENTS.md                        # This file
```

---

## File Inventory

### Root HTML Pages (18 files)
| File | Purpose | Key Sections |
|------|---------|--------------|
| `index.html` | Homepage | Hero with Three.js animation, services grid, testimonials, stats counter, CTA |
| `about.html` | Company info | Company story, team, values |
| `contact.html` | Lead capture | Contact form with validation, Google Maps embed, business hours |
| `blog.html` | Blog index | Grid of blog article cards |
| `projects.html` | Portfolio index | Grid of project category cards |
| `testimonials.html` | Social proof | Google reviews, client testimonials |
| `products.html` | Partners | Vendor logos and product categories |
| `locations.html` | Service areas | List of cities served |
| `kitchen-remodeling.html` | Service page | Service details, process, gallery, CTA |
| `bathroom-remodeling.html` | Service page | Service details, process, gallery, CTA |
| `home-remodeling.html` | Service page | Service details, process, gallery, CTA |
| `home-additions.html` | Service page | Service details, process, gallery, CTA |
| `adu.html` | Service page | ADU-specific content, regulations info |
| `exterior-remodeling.html` | Service page | Service details, process, gallery, CTA |
| `custom-homes.html` | Service page | Custom home building process |
| `commercial-remodeling.html` | Service page | Commercial services |
| `design-build.html` | Service page | Design-build process explanation |
| `privacy-policy.html` | Legal | Privacy policy text |
| `terms-of-use.html` | Legal | Terms of use text |

### Blog Articles (6 files in `/blog`)
| File | Topic | Related Service |
|------|-------|-----------------|
| `kitchen-remodeling-trends-2025.html` | 2025 kitchen trends | Kitchen Remodeling |
| `kitchen-cabinets-guide.html` | Cabinet buying guide | Kitchen Remodeling |
| `bathroom-design-ideas.html` | Bathroom design inspiration | Bathroom Remodeling |
| `home-remodeling-guide-2025.html` | Complete remodeling guide | Home Remodeling |
| `home-addition-ideas.html` | Home addition inspiration | Home Additions |
| `adu-building-guide.html` | ADU construction guide | ADU |

### Project Galleries (5 files in `/projects`)
| File | Category | Image Assets Used |
|------|----------|-------------------|
| `kitchen-remodeling.html` | Kitchen projects | `kitchen-*.jpg` |
| `bathroom-remodeling.html` | Bathroom projects | `bathroom-*.jpg` |
| `complete-home-remodeling.html` | Whole home projects | `home-*.jpg` |
| `condo-remodeling.html` | Condo projects | `condo-*.jpg` |
| `outdoor-remodeling.html` | Outdoor projects | `outdoor-*.jpg`, `backyard-*.jpg` |

---

## Architecture Details

### No Build System
This is a purely static site with **no build process**. All dependencies are loaded from CDNs directly in the HTML files.

### CDN Dependencies
```html
<!-- Tailwind CSS (runtime) -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<!-- Lucide Icons -->
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>

<!-- Three.js (homepage only) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<!-- GSAP + ScrollTrigger -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
```

### Tailwind Configuration (Inline in each file)
Every HTML file contains the same Tailwind config in a `<script>` tag:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: {
                    50: '#fdf9ed',
                    100: '#f9eecd',
                    200: '#f2db97',
                    300: '#ebc561',
                    400: '#e5b03d',   // Light gold (accents, hover)
                    500: '#c9922b',   // Primary gold (buttons, links)
                    600: '#a06f22',
                    700: '#80521f',
                    800: '#6b4320',
                    900: '#5c391f',
                },
                dark: {
                    900: '#1a1a1a',   // Primary dark (backgrounds)
                    800: '#2d2d2d',
                    700: '#404040',
                }
            },
            fontFamily: {
                'display': ['Playfair Display', 'serif'],  // Headings
                'body': ['Inter', 'sans-serif'],           // Body text
            }
        }
    }
}
```

### No Component System
Headers, footers, and navigation are **duplicated in every HTML file**. Any changes to shared elements must be manually replicated across all files.

**Shared elements to update across all files:**
- Top bar (license number, phone)
- Header navigation (desktop + mobile)
- Footer (contact info, service links, legal links)

---

## Page Templates & Patterns

### Standard Page Structure
Every page follows this structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags, title, favicon -->
    <!-- CDN imports (Tailwind, Fonts, Icons) -->
    <!-- Tailwind config script -->
    <!-- Custom styles -->
</head>
<body>
    <!-- Top Bar (license + phone) -->
    <!-- Header with navigation -->
    <!-- Mobile Menu (hidden by default) -->
    
    <!-- Hero Section -->
    <!-- Main Content Sections -->
    <!-- CTA Section -->
    
    <!-- Footer -->
    <!-- Back to Top Button -->
    
    <!-- JavaScript (Lucide init, mobile menu, scroll effects) -->
</body>
</html>
```

### URL Patterns for Subdirectories
Pages in subdirectories (`/blog`, `/projects`) use relative paths with `../`:
```html
<!-- From blog/article.html -->
<a href="../index.html">Home</a>
<img src="../assets/logo.png">
<a href="../contact.html">Contact</a>
```

### Common CSS Classes

| Class | Purpose |
|-------|---------|
| `.reveal` | Scroll-triggered fade-in animation |
| `.reveal.active` | Element is visible |
| `.nav-link` | Navigation link with underline hover effect |
| `.dropdown` | Dropdown container |
| `.dropdown-menu` | Dropdown content (hidden by default) |
| `.mobile-menu` | Mobile navigation panel |
| `.mobile-menu.active` | Mobile menu is open |
| `.service-card` | Service card with hover effects |
| `.testimonial-card` | Testimonial card with hover effects |
| `.img-zoom` | Container for zoom-on-hover images |
| `.form-input` | Form input with focus styles |
| `.form-input.error` | Input with validation error |
| `.info-card` | Contact info card with hover lift |
| `.gallery-card` | Project gallery card with overlay |
| `.hero-overlay` | Dark gradient overlay for hero images |
| `.font-display` | Playfair Display font |

### JavaScript Patterns

**Icon Initialization (required on every page):**
```javascript
lucide.createIcons();
```

**Mobile Menu Toggle:**
```javascript
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenuClose = document.getElementById('mobile-menu-close');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuBtn.addEventListener('click', () => mobileMenu.classList.add('active'));
mobileMenuClose.addEventListener('click', () => mobileMenu.classList.remove('active'));
```

**Scroll Reveal Animation:**
```javascript
const revealElements = document.querySelectorAll('.reveal');
const revealOnScroll = () => {
    revealElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        if (elementTop < window.innerHeight - 100) {
            element.classList.add('active');
        }
    });
};
window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);
```

**Counter Animation (homepage):**
```javascript
// Animates numbers from 0 to target value
// Uses data-target attribute: <span class="counter" data-target="500">0</span>
```

---

## Business Information

### Company Details
| Field | Value |
|-------|-------|
| Company Name | Maison Remodeling Group |
| Phone | 408-766-7272 |
| Email | info@maisonrg.com |
| Address | 1580 Oakland Rd, STE C106, San Jose, CA 95131 |
| License | #1097881 |
| Business Hours | Mon-Fri 9am-6pm, Sat-Sun Closed |

### Services Offered
1. Full Home Remodeling
2. Kitchen Remodeling
3. Bathroom Remodeling
4. Home Additions
5. ADU Construction
6. Exterior Remodeling
7. Custom Homes
8. Commercial Remodeling
9. Design Build

### Service Areas
**Bay Area:** San Jose, Santa Clara, Milpitas, Sunnyvale, Cupertino, Mountain View, Palo Alto, Los Altos, Saratoga, Campbell, Los Gatos, Fremont, Newark, San Mateo, Redwood City, Menlo Park, Hayward

**Orange County:** Laguna Beach, Santa Ana, Laguna Woods, Villa Park, Irvine, Newport Beach

---

## Common Development Tasks

### Adding a New Page

1. **Copy a template** - Use `about.html` for simple pages or a service page for service content
2. **Update head section:**
   ```html
   <title>Page Title | Maison Remodeling Group</title>
   <meta name="description" content="Page description for SEO">
   ```
3. **Update navigation** - Add link to both desktop nav and mobile menu
4. **Update breadcrumbs** (if applicable)
5. **Update all other pages** - Add new page to their navigation

### Adding a Blog Post

1. Create file in `blog/` directory
2. Use `blog/kitchen-remodeling-trends-2025.html` as template
3. Update paths to use `../` prefix for assets and links
4. Add article card to `blog.html` index
5. Add to "Related Articles" section in relevant blog posts

### Adding a Project Gallery

1. Create file in `projects/` directory
2. Use `projects/kitchen-remodeling.html` as template
3. Update paths to use `../` prefix
4. Add images to `assets/` with descriptive names
5. Add gallery card to `projects.html` index
6. Update Projects dropdown in all navigation menus

### Updating Contact Information

Update in ALL HTML files:
1. **Top bar:** `.bg-dark-900` section at top
2. **Header CTA:** Phone button and consultation button
3. **Footer:** Contact section with phone, email, address
4. **Contact page:** Sidebar contact info card

### Updating Navigation Menu

Update in ALL HTML files in TWO locations:
1. **Desktop nav:** Inside `<div class="hidden lg:flex items-center gap-8">`
2. **Mobile menu:** Inside `<div id="mobile-menu">`

### Adding a New Service

1. Create `[service-name].html` in root
2. Add to Services dropdown in all navigation menus
3. Add service card to homepage services section
4. Add to footer services list
5. Create corresponding project gallery in `projects/`
6. Consider creating related blog post in `blog/`

### Changing Brand Colors

Update the Tailwind config in EVERY HTML file:
```javascript
primary: {
    500: '#NEW_PRIMARY_COLOR',
    // ... update entire palette
}
```

---

## Form Handling

### Contact Form (`contact.html`)
- Client-side validation with JavaScript
- Fields: First Name, Last Name, Email, Phone, Project Type, Message, File Upload
- Validation shows `.error` class on invalid fields
- Success message displayed on submission
- **Note:** No backend - form submission is demo only

### Form Validation Pattern
```javascript
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    
    if (field.required && !value) isValid = false;
    if (field.type === 'email' && value && !emailRegex.test(value)) isValid = false;
    
    field.classList.toggle('error', !isValid);
    return isValid;
}
```

---

## SEO Considerations

### Meta Tags (every page)
```html
<title>Keyword-Rich Title | Maison Remodeling Group</title>
<meta name="description" content="150-160 character description with keywords">
<link rel="icon" type="image/png" href="assets/favicon.png">
```

### Image Alt Text
All images should have descriptive alt text:
```html
<img src="assets/kitchen-sanjose.jpg" alt="Modern kitchen remodel in San Jose with white cabinets">
```

### Internal Linking
- Service pages link to related projects
- Blog posts link to related services
- CTAs link to contact page

---

## Testing Checklist

### Functionality
- [ ] All internal links work
- [ ] All external links open in new tab
- [ ] Phone numbers are clickable (`tel:` links)
- [ ] Email links work (`mailto:` links)
- [ ] Contact form validation works
- [ ] Mobile menu opens/closes
- [ ] Dropdown menus work on hover
- [ ] Back to top button appears on scroll

### Visual
- [ ] Images load correctly
- [ ] Animations play smoothly
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] No horizontal scroll on mobile
- [ ] Fonts load correctly
- [ ] Icons display correctly

### Performance
- [ ] Images are optimized (compressed JPGs)
- [ ] No console errors
- [ ] Page loads in reasonable time

---

## Deployment

### Static Hosting Options
- Netlify (recommended - easy deployment)
- Vercel
- GitHub Pages
- AWS S3 + CloudFront
- Any web server (Apache, Nginx)

### Deployment Steps
1. No build step required
2. Upload all files maintaining directory structure
3. Ensure `index.html` is served at root
4. Configure custom domain if needed
5. Enable HTTPS

### Files to Deploy
```
/
├── assets/
├── blog/
├── projects/
├── *.html (all root HTML files)
├── llm.txt
└── AGENTS.md (optional)
```

---

## Gotchas & Known Issues

1. **No component system** - Changes to header/footer must be made in ALL files
2. **Tailwind via CDN** - Config must be duplicated in every file
3. **Relative paths** - Subdirectory pages need `../` prefixes
4. **Form has no backend** - Contact form is demo only
5. **Three.js only on homepage** - Don't include on other pages (performance)
6. **Icon initialization required** - Must call `lucide.createIcons()` on every page
7. **Google Maps embed** - May need API key for production

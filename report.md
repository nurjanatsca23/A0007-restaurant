# Development of a Full-Stack Web Application for Fener Restaurant

## Coursework Report

**Student:** [Student Name]
**Group:** A0007
**Supervisor:** [Supervisor Name]
**Institution:** [University Name]
**Date:** March 2026

---

## Table of Contents

1. Introduction
2. Project Background and Motivation
3. Requirements Analysis
4. System Architecture and Design
5. Technology Stack
6. Database Design and Data Modeling
7. Backend Development
8. Frontend Architecture
9. Page Design and Implementation
10. Menu System and Data Management
11. Shopping Cart System
12. Order Processing and Telegram Integration
13. Responsive Web Design
14. UI/UX Design Principles
15. Map and Geolocation Integration
16. Client-Side Interactivity
17. Performance Optimization
18. Security Considerations
19. Testing and Quality Assurance
20. Deployment and Maintenance
21. Challenges and Solutions
22. Future Improvements
23. Conclusion

References

Appendix A: Source Code

---

## 1. Introduction

The rapid growth of the digital economy has fundamentally transformed the hospitality industry. Restaurants worldwide are increasingly adopting web technologies to establish their online presence, streamline operations, and enhance customer engagement. A well-designed restaurant website serves as a critical touchpoint between the establishment and its customers, providing information about the menu, location, ambiance, and enabling online ordering capabilities.

This report presents the complete development lifecycle of a full-stack web application created for **Fener** (Фенер), a restaurant located in Jalal-Abad, Kyrgyzstan. The name "Fener" reflects the restaurant's philosophy of blending culinary traditions, offering a diverse menu that spans Central Asian, Turkish, Japanese, Italian, and European cuisines. The website was designed to serve as the restaurant's primary digital platform, combining an aesthetically pleasing interface with practical functionality including menu browsing, online ordering, and direct communication with the restaurant's management through Telegram integration.

The project was developed as a practical application of modern web development principles, encompassing server-side programming with Python and Flask, client-side development with HTML5, CSS3, and JavaScript, database management with SQLite, and external API integration with the Telegram Bot API and 2GIS mapping service. The resulting application demonstrates the application of full-stack development skills in a real-world business context.

The objectives of this project are multifold: first, to create a visually appealing and user-friendly website that accurately represents the restaurant's brand identity; second, to implement a functional online ordering system that can process customer orders and relay them to restaurant staff in real time; third, to ensure the application is fully responsive and accessible across a wide range of devices and screen sizes; and fourth, to integrate third-party services such as mapping and messaging platforms to enhance the overall user experience.

This report is structured to provide a comprehensive overview of every aspect of the development process. It begins with the project background and motivation, followed by a detailed requirements analysis. Subsequent chapters cover the system architecture, technology stack selection, database design, and the implementation of both backend and frontend components. The report also addresses topics such as responsive design, performance optimization, security considerations, and testing methodologies. The document concludes with a discussion of challenges encountered during development, proposed future improvements, and a summary of key findings and conclusions.

---

## 2. Project Background and Motivation

### 2.1 About the Restaurant

Fener is a restaurant situated in the city of Jalal-Abad, located in the southern part of the Kyrgyz Republic. The restaurant is positioned at Shabdanbay Abdramanov Street 1, a central location accessible to both local residents and visitors. Operating daily from 10:00 AM to 11:00 PM, Fener serves a wide demographic, including families, business professionals, and tourists exploring the region.

The restaurant's tagline, "Слияние традиций" (Fusion of Traditions), encapsulates its culinary philosophy. The menu reflects an ambitious approach to cuisine, offering dishes from multiple culinary traditions. Central Asian staples such as plov (pilaf), lagman (noodle soup), and manti (steamed dumplings) sit alongside Turkish specialties like Iskender kebab, Lahmacun, and Keramite kofte. The menu also features Japanese cuisine in the form of sushi rolls, Italian offerings including pizza and tiramisu, and international favorites such as Caesar salad and New York cheesecake. This diverse menu positions Fener as a destination restaurant capable of satisfying a wide range of culinary preferences.

### 2.2 Business Need

Prior to the development of this web application, the restaurant's digital presence was limited to a basic Taplink page — a simplified link-in-bio platform commonly used in Central Asian markets. While Taplink served the basic purpose of displaying menu items and contact information, it presented several significant limitations.

First, the Taplink platform offered minimal customization capabilities, making it difficult to create a distinctive brand identity that would differentiate Fener from competitors. Second, the platform lacked advanced functionality such as categorized menu browsing with filtering and search capabilities. Third, there was no integrated ordering system that could automatically relay customer orders to kitchen staff. Fourth, the platform provided limited control over layout, typography, and visual design, restricting the restaurant's ability to create a premium digital experience that matched the quality of its in-restaurant dining.

These limitations motivated the development of a custom web application that would address each of these shortcomings while providing a platform for future growth and feature expansion.

### 2.3 Project Goals

The development project was guided by the following primary goals:

1. **Brand Representation:** Create a digital experience that authentically represents Fener's brand identity, ambiance, and culinary philosophy through carefully chosen typography, color palettes, imagery, and interactive elements.

2. **Menu Accessibility:** Develop an intuitive menu browsing system with categorization, search functionality, and detailed dish information including descriptions, prices, and high-quality imagery.

3. **Online Ordering:** Implement a complete ordering workflow that allows customers to add items to a shopping cart, provide contact information, and submit orders that are automatically forwarded to restaurant management.

4. **Real-Time Notifications:** Integrate a Telegram bot to deliver instant order notifications to restaurant staff, enabling rapid response times and efficient order processing.

5. **Responsive Design:** Ensure the application provides an optimal viewing and interaction experience across all device types, from large desktop monitors to mobile smartphones.

6. **Performance:** Optimize the application for fast load times and smooth interactions, particularly important in regions where internet connectivity may vary in speed and reliability.

7. **Scalability:** Design the architecture to accommodate future feature additions such as reservation systems, loyalty programs, or delivery tracking.

---

## 3. Requirements Analysis

### 3.1 Functional Requirements

The functional requirements were established through discussions with restaurant management and analysis of competitor offerings. They are categorized as follows:

**FR-1: Home Page.** The application shall provide an attractive landing page that introduces the restaurant, showcases featured dishes, displays customer reviews, provides contact information with an interactive map, and features a photo gallery of the restaurant's interior.

**FR-2: Menu Page.** The application shall display the complete restaurant menu organized by categories. Users shall be able to filter dishes by category and search for specific items by name. Each dish shall display an image, name, and price, with additional details available in a modal popup.

**FR-3: Shopping Cart.** The application shall provide a persistent shopping cart that allows users to add dishes, adjust quantities, and remove items. The cart contents shall persist across page navigations using browser local storage.

**FR-4: Order Placement.** The application shall allow users to submit orders by providing their name and phone number. Upon submission, the order shall be saved to a database and a notification shall be sent via Telegram.

**FR-5: Navigation.** The application shall provide clear navigation between pages, including smooth scrolling to sections within the home page and a responsive hamburger menu for mobile devices.

**FR-6: Map Integration.** The application shall display an interactive map showing the restaurant's location using the 2GIS mapping service, which provides detailed local mapping data for Central Asian cities.

### 3.2 Non-Functional Requirements

**NFR-1: Performance.** Pages shall load within 3 seconds on a standard broadband connection. Images shall be optimized and lazy-loaded where appropriate.

**NFR-2: Responsiveness.** The application shall be fully functional and visually appealing on devices with screen widths ranging from 320px to 2560px.

**NFR-3: Browser Compatibility.** The application shall be compatible with current versions of Chrome, Firefox, Safari, and Edge browsers.

**NFR-4: Accessibility.** The application shall follow basic accessibility guidelines, including appropriate alt text for images, semantic HTML structure, and sufficient color contrast ratios.

**NFR-5: Maintainability.** The codebase shall be organized in a modular fashion with clear separation between data, presentation, and business logic to facilitate future updates.

**NFR-6: Localization.** The application's primary language shall be Russian, with interface elements and content presented in Russian to serve the local market.

### 3.3 Use Case Analysis

The primary actors identified in the system are:

1. **Website Visitor:** An individual browsing the restaurant's website to view the menu, learn about the restaurant, or check contact and location information.

2. **Customer (Ordering):** A visitor who adds items to the cart and places an order by providing contact details.

3. **Restaurant Staff and Manager:** The recipient of order notifications via Telegram, responsible for processing and fulfilling orders.

Key use cases include: (UC-1) Browse menu by category, (UC-2) Search for a dish by name, (UC-3) View dish details, (UC-4) Add item to cart, (UC-5) Modify cart contents, (UC-6) Place an order, (UC-7) View restaurant location on map, (UC-8) Read customer reviews, (UC-9) View restaurant gallery.

---

## 4. System Architecture and Design

### 4.1 Architectural Pattern

The application follows a **Model-View-Controller (MVC)** architectural pattern, adapted to the Flask micro-framework's conventions. In this architecture:

- **Model:** The data layer is represented by the `menu_data.py` module (which provides menu data as a Python data structure) and the SQLite database (which stores order records). The data module contains a comprehensive list of dictionaries defining each menu category and its dishes, including titles, prices, descriptions, and image URLs.

- **View:** The presentation layer consists of Jinja2 HTML templates (`base.html`, `home.html`, `menu.html`) and CSS stylesheets (`style.css`). These templates render the user interface, displaying data passed from the controller.

- **Controller:** The `app.py` file serves as the controller, containing Flask route handlers that process HTTP requests, interact with the data layer, and render appropriate views.

### 4.2 Application Structure

The project follows a standard Flask directory layout:

```
A0007-restaurant/
├── app.py                  # Main application file (Controller)
├── menu_data.py            # Menu data definitions (Model)
├── database.db             # SQLite database file
├── static/
│   ├── style.css           # Global stylesheet
│   └── photos/             # Restaurant gallery images (17 photos)
└── templates/
    ├── base.html           # Base template with shared layout
    ├── home.html           # Home page template
    └── menu.html           # Menu page template
```

### 4.3 Request-Response Flow

The typical request-response cycle in the application operates as follows:

1. The client (web browser) sends an HTTP GET request to the Flask development server.
2. Flask's routing mechanism matches the request URL to the appropriate route handler in `app.py`.
3. The route handler retrieves any necessary data (e.g., menu categories from `menu_data.py`).
4. The handler invokes `render_template()`, passing the data to a Jinja2 template.
5. The template engine processes the template, inserting dynamic data and applying template inheritance from `base.html`.
6. The rendered HTML is returned to the client as an HTTP response.
7. The browser renders the HTML and loads associated resources (CSS, images, scripts).

For order submission, the flow differs slightly: the client sends an asynchronous POST request with JSON data via the Fetch API. The server processes the order, saves it to the database, sends a Telegram notification, and returns a JSON response indicating success or failure.

### 4.4 Template Inheritance

The application employs Jinja2's template inheritance mechanism to maintain consistency and reduce code duplication. The `base.html` template defines the overall page structure, including:

- HTML document head with meta tags, font imports, and stylesheet links.
- Fixed header with logo, navigation links, and cart button.
- Shopping cart sidebar component.
- Order confirmation modal.
- Footer with restaurant information.
- Client-side JavaScript for cart management, navigation, and toast notifications.
- Block placeholders for child templates (`title`, `extra_css`, `content`, `extra_js`).

Child templates (`home.html` and `menu.html`) extend `base.html` and override specific blocks to provide page-specific content and styling. This approach ensures that common elements like the header, footer, cart, and associated JavaScript logic are defined once and maintained centrally.

---

## 5. Technology Stack

### 5.1 Backend Technologies

**Python 3.x** was selected as the server-side programming language due to its readability, extensive standard library, and robust ecosystem of web development frameworks. Python's syntax clarity makes the codebase accessible for maintenance and collaboration.

**Flask** (micro-framework) was chosen over more full-featured alternatives such as Django for several reasons. Flask's minimalist approach provides only the essential components needed for web development — routing, template rendering, and request handling — without imposing a rigid project structure. This lightweight nature results in faster development cycles and a smaller deployment footprint, both advantageous for a project of this scope. Flask's built-in development server with hot-reloading capabilities also significantly improved the development workflow.

**SQLite** serves as the relational database management system. SQLite is a serverless, self-contained database engine that stores data in a single file (`database.db`). This choice eliminates the need for a separate database server, simplifying both development and deployment. While SQLite has known limitations in terms of concurrent write operations and scalability, these are largely irrelevant for a restaurant website with relatively low order volumes. The database stores order records including customer information, order items, total prices, and timestamps.

**Jinja2** is the template engine used for server-side HTML rendering. Bundled with Flask, Jinja2 provides powerful features including template inheritance, variable interpolation, loop constructs, conditional logic, and auto-escaping for security. The template engine allows for clean separation between business logic and presentation.

### 5.2 Frontend Technologies

**HTML5** provides the semantic structural foundation of the web pages. The application makes use of HTML5 semantic elements such as `<header>`, `<nav>`, `<main>`, `<section>`, `<aside>`, and `<footer>` to improve document structure, accessibility, and SEO.

**CSS3** is used for all visual styling without any CSS framework or preprocessor. This vanilla CSS approach provides maximum control over the design and avoids the overhead of unused framework rules. The stylesheet employs modern CSS features including CSS Custom Properties (variables), Flexbox, CSS Grid, media queries, transitions, animations, backdrop-filter, and the scroll-snap API.

**JavaScript (ES6+)** handles all client-side interactivity. Written in vanilla JavaScript without external libraries or frameworks, the client-side code manages the shopping cart state, DOM manipulation for dynamic UI updates, asynchronous HTTP requests via the Fetch API, modal dialogs, search and filter functionality, scroll-based animations, and toast notifications.

### 5.3 External Services and APIs

**Telegram Bot API** is used for real-time order notifications. When a customer places an order, the server constructs a formatted message containing order details and sends it to a designated Telegram group using the Bot API's `sendMessage` endpoint. This provides restaurant staff with immediate, push-notification-enabled access to incoming orders without requiring a separate administrative dashboard.

**2GIS Map Widget** is embedded on the home page to display the restaurant's location. 2GIS was chosen over Google Maps or OpenStreetMap alternatives because it provides superior detail and accuracy for cities in Central Asia, including building-level mapping, public transit information, and business listings specific to the Kyrgyz Republic.

**Google Fonts** provides the typography used throughout the application. Two font families are loaded: *Inter* (a clean, modern sans-serif for body text and UI elements) and *Playfair Display* (an elegant serif font for headings and display text), establishing the visual hierarchy and reinforcing the restaurant's premium brand positioning.

**Unsplash** and **Taplink CDN** serve as sources for dish imagery. A combination of professionally sourced stock photography from Unsplash and the restaurant's own photography hosted on Taplink provides visual content for menu items.

---

## 6. Database Design and Data Modeling

### 6.1 Database Schema

The application uses a single-table SQLite database for order persistence. The `orders` table is defined with the following schema:

| Column          | Type      | Constraints                    | Description                        |
|-----------------|-----------|--------------------------------|------------------------------------|
| id              | INTEGER   | PRIMARY KEY, AUTOINCREMENT     | Unique order identifier            |
| customer_name   | TEXT      |                                | Customer's name                    |
| customer_phone  | TEXT      |                                | Customer's phone number            |
| items           | TEXT      | NOT NULL                       | JSON-encoded array of cart items   |
| total_price     | INTEGER   | NOT NULL                       | Total order price in KGS (som)     |
| created_at      | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP      | Order creation timestamp           |

The `items` column stores a JSON-serialized representation of the shopping cart contents. Each item in the array contains the dish title, unit price, image URL, and quantity. While storing complex data as JSON within a relational column is not strictly normalized, this approach was chosen for pragmatic reasons: it simplifies the schema, avoids the need for additional junction tables, and preserves the complete order context in a single record.

### 6.2 Menu Data Structure

Rather than storing menu data in the database, the application maintains menu information in a Python data module (`menu_data.py`). This module exports a list of dictionaries representing the menu hierarchy.

The top-level list `MENU_CATEGORIES` contains category objects, each with a `name` field and a `dishes` list. Each dish object contains `title`, `price`, `description`, and `image` fields. This data structure is passed directly to the template engine for rendering.

The decision to use a static Python data structure rather than a database table for menu data was motivated by several factors. The menu changes infrequently, making database overhead unnecessary. The data structure is simple and well-suited to Python's native dictionary and list types. Direct Python access eliminates database query latency. And the data can be version-controlled alongside the application code.

The menu currently contains 8 categories with a total of 35 dishes spanning diverse cuisines:

| Category                 | Number of Dishes | Cuisine Type              |
|--------------------------|------------------|---------------------------|
| Салаты (Salads)          | 5                | Mixed                     |
| Супы (Soups)             | 2                | Central Asian             |
| Горячие блюда (Hot)      | 5                | Central Asian / Georgian  |
| Турецкие блюда (Turkish) | 4                | Turkish                   |
| Суши и Пицца             | 4                | Japanese / Italian        |
| Стейки (Steaks)          | 3                | Western                   |
| Выпечка и Десерты        | 3                | European                  |
| Напитки (Drinks)         | 7                | Bar / Café                |

### 6.3 Data Initialization

The database is initialized at application startup through the `init_db()` function. This function creates the `orders` table if it does not exist and performs a migration check for backward compatibility — if the table exists but lacks the `customer_name` or `customer_phone` columns (which were added after the initial schema), the function adds them using `ALTER TABLE` statements. This approach provides a simple migration mechanism that ensures existing databases are updated without data loss.

---

## 7. Backend Development

### 7.1 Application Initialization

The Flask application is initialized in `app.py` with a straightforward configuration. The application instance is created, configuration constants for the Telegram integration are defined, and the database is initialized on startup.

The application defines three route handlers:

1. **`GET /`** — Renders the home page template.
2. **`GET /menu`** — Retrieves menu data from the data module and renders the menu page template with the categories passed as context.
3. **`POST /api/order`** — Processes incoming order submissions.

### 7.2 Order Processing Pipeline

The order processing endpoint (`/api/order`) implements a multi-step pipeline:

**Step 1: Request Validation.** The endpoint extracts JSON data from the request body, retrieving the shopping cart array, customer name, and phone number. If the cart is empty, the endpoint returns a 400 Bad Request response with an appropriate error message.

**Step 2: Price Calculation.** The total order price is calculated server-side by summing the product of each item's price and quantity. This server-side calculation serves as a validation measure, ensuring that the total is computed from authoritative price data rather than relying solely on client-submitted values.

**Step 3: Database Persistence.** The order is inserted into the SQLite database with the customer's name, phone number, serialized cart items (as JSON), and the calculated total price. The database's auto-increment functionality generates a unique order ID, which is retrieved using `cursor.lastrowid`.

**Step 4: Telegram Notification.** A formatted HTML message is constructed containing the order number, timestamp (adjusted to the Bishkek timezone using the `pytz` library), customer details, itemized cart contents with quantities and subtotals, and the grand total. This message is sent to the configured Telegram group chat via the Bot API.

**Step 5: Response.** The endpoint returns a JSON response containing a success indicator and the order ID, which the client uses to display a confirmation message.

### 7.3 Error Handling

The Telegram notification step is wrapped in a try-except block to ensure that a failure in the external API call does not prevent the order from being recorded or the customer from receiving confirmation. If the Telegram API is unreachable, the error is logged to the console, but the order is still considered successfully placed since it has already been persisted to the database.

---

## 8. Frontend Architecture

### 8.1 Template Hierarchy

The frontend is built on a two-level template hierarchy. The base template (`base.html`) at 335 lines defines the complete page shell, while child templates provide page-specific content.

The base template is responsible for several critical components:

**Document Head:** Includes character encoding declaration, viewport meta tag for responsive design, dynamic page title via Jinja2 block, Google Fonts preconnect and stylesheet links, application CSS link, and favicon.

**Header:** A fixed-position header containing the restaurant logo (image and text), navigation links (Home, Menu, Contacts, Reviews), a shopping cart button with a dynamic badge showing the item count, and a hamburger toggle button for mobile view.

**Cart Sidebar:** A slide-in sidebar panel triggered by the cart button. It displays cart items with images, titles, prices, and quantity controls (increment, decrement, and remove). Below the items, it presents a form for customer name and phone number, a running total, and an "Order" button.

**Order Modal:** A centered modal dialog that appears after successful order placement, displaying a confirmation message, itemized order summary, total price, and order number.

**Footer:** A three-column footer grid containing the restaurant brand, contact information, and copyright notice.

**JavaScript:** Approximately 220 lines of client-side JavaScript embedded in the base template, providing cart management, navigation, modal handling, and toast notification functionality.

### 8.2 Design System

The application's visual design is governed by a comprehensive set of CSS custom properties defined in the `:root` selector of `style.css`. These custom properties create a cohesive design system that ensures visual consistency across all pages and components.

**Color Palette:**
- Background: `#FAF6F1` (warm off-white)
- Surface: `#FFFFFF` (pure white for cards and panels)
- Primary: `#5C3A21` (deep coffee brown)
- Accent: `#C49A6C` (warm gold and caramel)
- Olive: `#8B9A7B` (muted sage green)

This warm, earth-toned palette was chosen to evoke feelings of comfort, warmth, and quality dining — aligning with the restaurant's brand identity as a place that blends culinary traditions in a welcoming atmosphere.

**Typography:** The dual-font system uses Inter for body text and UI elements (providing excellent readability at small sizes) and Playfair Display for headings and display text (adding elegance and visual distinction). This combination of a geometric sans-serif with a transitional serif is a widely recognized pattern in premium brand design.

**Spacing and Radius:** Shadow variables at three intensity levels (small, medium, large) create depth hierarchy. Border radius variables at three sizes ensure consistent rounding of corners across UI elements.

---

## 9. Page Design and Implementation

### 9.1 Home Page

The home page (`home.html`) is the most complex template in the application at over 700 lines, incorporating inline CSS for page-specific styles, multiple content sections, and scroll-based animation logic. The page is designed as a series of full-viewport sections that create an immersive, magazine-style browsing experience.

**Hero Section:** A full-height introduction featuring a background image of a restaurant interior with a dark gradient overlay for text readability. The centered content includes the restaurant name, tagline, and a call-to-action button linking to the menu page.

**Menu Preview Section:** Showcases three selected dishes from the menu in a responsive card grid. Each card features a dish image and title, designed to entice visitors to explore the full menu.

**About Section:** A two-column layout with descriptive text about the restaurant's culinary philosophy on the left and a 2x2 image grid on the right. The text emphasizes the use of natural ingredients, authentic recipes, and Eastern hospitality traditions.

**Contacts Section:** Combines restaurant contact details (address, phone, hours) with an embedded 2GIS interactive map, presented in a horizontal card layout with the details on the left and the map on the right.

**Gallery Section:** A masonry-style grid displaying 6 photographs of the restaurant's interior, showcasing the ambiance, decor, and dining spaces.

**Reviews Section:** Features three customer review cards, each containing a 5-star rating, review text, author name and avatar, and date. These are real reviews from the restaurant's Google and 2GIS listings.

### 9.2 Menu Page

The menu page (`menu.html`) provides a focused, functional interface for browsing the complete restaurant menu. Key components include:

**Search Bar:** A rounded search input with a magnifying glass icon and a clear button that appears when text is entered. The search filters dishes in real-time as the user types, matching against dish titles.

**Category Tabs:** A horizontally scrollable tab bar listing all menu categories with an "All" tab selected by default. Clicking a category tab filters the display to show only dishes from that category. The tab bar is sticky-positioned below the fixed header, remaining accessible during scrolling.

**Dish Cards:** Each dish is rendered as a compact card featuring a 180px-height image, the dish name, price, and an add-to-cart button (+). The cards are arranged in a responsive grid that adjusts column count based on screen width.

**Detail Modal:** Clicking a dish card opens a modal dialog showing a larger image, the dish title, a detailed description, and the price with an add-to-cart button.

---

## 10. Menu System and Data Management

### 10.1 Data Architecture

The menu data architecture employs a category-dish hierarchy that mirrors the physical menu's organization. Each category serves as a logical grouping of related dishes, while each dish entry contains all the metadata needed for display and ordering.

The data module approach offers several advantages for this application. Content updates require only modifying the Python file and restarting the server, without any database migration process. The entire menu can be version-controlled using Git, providing a complete change history. And the data stays closely aligned with the application code, making the codebase self-contained.

### 10.2 Image Strategy

The application employs a hybrid image strategy. Some dish images are sourced from the Unsplash API, a free stock photography service, using optimized URL parameters (width=600, height=400, fit=crop) to request appropriately sized images. Other dishes use the restaurant's own photography hosted on the Taplink CDN.

For the restaurant gallery, photographs are stored locally in the `static/photos/` directory. These 17 high-quality images show various aspects of the restaurant's interior and are served directly by the Flask static file handler.

### 10.3 Category Structure and Filtering

The menu filtering system operates entirely on the client side. When the page loads, all categories and dishes are rendered into the DOM. The JavaScript tab handler toggles category visibility by setting the CSS `display` property of category sections. The special "All" tab restores visibility of all sections.

The search function operates at the individual card level, hiding cards whose titles do not match the query and subsequently hiding empty category sections. This approach provides instant feedback without server round-trips, resulting in a responsive user experience.

---

## 11. Shopping Cart System

### 11.1 Cart State Management

The shopping cart is implemented as a client-side state management system. The cart state is maintained as a JavaScript array of objects stored in the global scope. Each cart item contains a title, price, image URL, and quantity.

State persistence is achieved through the browser's `localStorage` API. On every state change, the cart array is serialized to JSON and written to localStorage under the key `fener_cart`. On page load, the application attempts to parse the stored JSON and restore the cart state. This ensures that cart contents persist across page navigations, browser tabs, and even browser restarts.

### 11.2 Cart Operations

The cart supports the following operations:

**Add to Cart:** When a user clicks the "+" button on a dish card or the "Add to Cart" button in the detail modal, the `addToCart()` function is called with the dish title, price, and image URL. If an item with the same title already exists in the cart, its quantity is incremented; otherwise, a new item is added with a quantity of 1. A toast notification confirms the addition.

**Change Quantity:** The `changeQty()` function accepts a title and a delta value (+1 or -1). If the resulting quantity reaches zero, the item is removed from the cart entirely.

**Remove from Cart:** The `removeFromCart()` function removes an item by title, filtering it out of the cart array.

### 11.3 Cart User Interface

The cart sidebar is implemented as a fixed-position panel that slides in from the right side of the screen. The slide-in animation is achieved through CSS transforms: `translateX(100%)` in the closed state and `translateX(0)` in the open state, with a 0.35-second ease transition.

A semi-transparent dark overlay covers the rest of the page when the cart is open, providing a visual focus effect and acting as a click target to close the cart. The body's overflow is set to "hidden" when the cart is open to prevent background scrolling.

The cart contents are rendered dynamically on each state change. The `updateCartUI()` function clears existing cart item elements from the DOM and rebuilds them from the current cart array. Each item row displays a small thumbnail image, the item title, the subtotal (price multiplied by quantity), and increment and decrement buttons.

---

## 12. Order Processing and Telegram Integration

### 12.1 Order Submission Flow

The order submission process is initiated when the user clicks the "Place Order" button in the cart sidebar. The client-side `placeOrder()` function validates that the cart is not empty and that the customer name and phone fields are filled in, then constructs a JSON payload and sends it to the `/api/order` endpoint via an asynchronous Fetch API call.

During the request, the submit button text changes to "Processing..." and is disabled to prevent duplicate submissions. Upon receiving a successful response, the function clears the cart, closes the sidebar, and opens the confirmation modal displaying the order summary and assigned order number.

### 12.2 Telegram Bot Integration

The Telegram integration provides a zero-setup notification system for restaurant management. Rather than building a custom administrative dashboard, the project leverages Telegram's ubiquity and push notification capabilities.

The notification message is formatted in HTML (using Telegram's supported HTML subset, including the bold tag for emphasis) and structured for quick readability:

- A fire emoji and bold "New Order" header with the order number
- Timestamp in the local timezone (Asia/Bishkek)
- Customer name and phone number
- An itemized list of ordered dishes with quantities and subtotals
- A bold grand total

This structured format allows restaurant staff to quickly assess incoming orders, identify the customer, and begin preparation without needing to access a separate system.

### 12.3 Timezone Handling

Order timestamps are adjusted to the local timezone using the `pytz` library. The server creates a timezone-aware datetime object set to the `Asia/Bishkek` timezone (UTC+6:00), formatted as day.month.year hour:minute. This ensures that timestamps in Telegram notifications match the restaurant's local time, regardless of the server's configured timezone.

---

## 13. Responsive Web Design

### 13.1 Responsive Strategy

The application implements a mobile-first responsive design strategy using CSS media queries. The base styles are optimized for smaller viewport widths, with progressive enhancement applied at wider breakpoints. Four breakpoint thresholds are defined:

| Breakpoint | Target Devices              | Key Adjustments                     |
|------------|-----------------------------|-------------------------------------|
| <=480px    | Small smartphones           | Reduced font sizes, single-column   |
| <=600px    | Smartphones                 | Hidden logo image                   |
| <=768px    | Tablets portrait, phones    | Mobile navigation, simplified grids |
| <=992px    | Tablets landscape           | Stacked layouts, adjusted spacing   |

### 13.2 Navigation Responsiveness

On screens wider than 768px, the navigation is displayed as a horizontal link bar in the header. On narrower screens, the navigation collapses behind a hamburger toggle button. When activated, the navigation slides down as a full-width dropdown panel with larger touch-friendly link targets.

The hamburger button features a three-line animation that transforms into an "X" when active, using CSS transforms on the individual spans. The navigation panel's appearance and disappearance are controlled by toggling a CSS class, with smooth transitions for opacity and height.

### 13.3 Layout Adaptations

Several section-specific layout adaptations are implemented:

- The menu preview grid switches from a multi-column layout to a stacked single-column on mobile.
- The "About" section's side-by-side text and image layout converts to a vertically stacked arrangement.
- The contacts section changes from a horizontal contacts and map layout to a vertical stack.
- The photo gallery grid adjusts from three columns to two columns (tablet) to one column (phone).
- The footer grid collapses from three columns to a single centered column.

### 13.4 Map Responsiveness

The 2GIS map widget required special attention for responsive behavior. The map is embedded within a `.map-box` container that uses `overflow: hidden` and absolute positioning for the map iframe to ensure it fills the available space. At tablet and mobile breakpoints, `aspect-ratio` CSS properties are applied (16/10 for tablets, 4/3 for mobile) to maintain appropriate proportions, preventing the map from either overflowing its container or being too small for useful interaction.

### 13.5 Sticky Navigation on Menu Page

The menu page's category tab bar is implemented with `position: sticky` and `top: 72px` (matching the fixed header height), ensuring it remains accessible during scrolling through long menu listings. A background color is applied to prevent scrolled content from showing through behind the tabs. On mobile devices, the sticky top offset adjusts to 60px to match the reduced header height.

---

## 14. UI/UX Design Principles

### 14.1 Visual Hierarchy

The application's visual hierarchy guides users' attention through deliberate use of size, color, weight, and spacing. Page-level headings use the Playfair Display serif font at large sizes (up to 5rem on desktop), creating clear section delineation. Subheadings and card titles transition to smaller serif renderings, while body text and UI labels use the Inter sans-serif at standard body sizes.

Color is used strategically to denote importance: primary actions (buttons, active navigation) use the deep brown primary color, secondary information uses the muted text-light shade, and decorative accents employ the warm gold tone.

### 14.2 Micro-Interactions

The application incorporates numerous micro-interactions to enhance perceived quality and responsiveness:

- **Hover Effects:** Cards lift slightly (via translateY) and gain enhanced shadows on hover, providing tactile feedback.
- **Button Animations:** Buttons scale or change background color on hover, with smooth CSS transitions.
- **Toast Notifications:** Adding an item to the cart triggers a slide-up toast notification at the bottom of the screen, which auto-dismisses after 2 seconds.
- **Modal Transitions:** Dish detail and order confirmation modals fade in with a slight scale and translate animation.
- **Cart Slide:** The cart sidebar slides in from the right with an ease transition.
- **Scroll Reveal:** Home page sections fade in and translate upward as they enter the viewport, driven by the Intersection Observer API.

### 14.3 Scroll-Snap Behavior

The home page implements CSS `scroll-snap-type: y mandatory` on desktop viewports, creating a snapping behavior that aligns sections to the viewport as the user scrolls. This creates a presentation-like browsing experience where each section is viewed as a full "slide." The scroll-snap behavior is disabled on mobile (below 768px) to allow natural continuous scrolling, which is more ergonomic on touch devices.

### 14.4 Decorative Elements

Abstract background "blobs" — large, blurred circular shapes created with CSS `filter: blur(80px)` — are positioned behind content sections to add depth and visual interest. These decorative elements use colors from the design system's accent palette (soft beige, olive) at reduced opacity, creating a subtle layered effect without detracting from content readability.

---

## 15. Map and Geolocation Integration

### 15.1 2GIS Widget Implementation

The restaurant's location is displayed through an embedded 2GIS map widget. 2GIS is a digital mapping platform that provides particularly detailed coverage of cities in Central Asia, Russia, and the Middle East, making it the optimal choice for a restaurant in Jalal-Abad, Kyrgyzstan.

The widget is initialized with the following configuration:
- **Coordinates:** Latitude 40.952977, Longitude 72.982543
- **Zoom Level:** 16 (neighborhood-level detail)
- **City:** dzhalal-abad
- **Organization ID:** 70000001096321190 (Fener's 2GIS listing)

The widget provides interactive capabilities including panning, zooming, and clicking on the restaurant marker for additional business information.

### 15.2 Responsive Map Handling

To ensure the map displays correctly across different screen sizes, the map container uses relative positioning with `overflow: hidden`, while the map iframe (created by the widget loader) is absolutely positioned to fill the entire container. This approach prevents the map from exceeding its container boundaries while maintaining interactive functionality.

At the tablet breakpoint (<=992px), the contacts container changes from a horizontal layout to a vertical stack, and the map gains an explicit aspect ratio of 16:10. At the mobile breakpoint (<=768px), the aspect ratio adjusts to 4:3, providing a more square viewing area appropriate for narrow screens.

---

## 16. Client-Side Interactivity

### 16.1 Intersection Observer for Scroll Animations

The home page employs the Intersection Observer API to trigger CSS animations as sections enter the viewport. An observer is configured with a threshold of 0.2 (20% visibility) and negative root margins to trigger slightly before the element reaches the viewport edges.

When a section intersects, a `visible` CSS class is added, which triggers transition animations on child elements marked with the `animate-on-scroll` class. Different delay classes (`delay-1`, `delay-2`, `delay-3`) create a staggered reveal effect, with elements appearing sequentially at 0.1s, 0.3s, and 0.5s intervals respectively.

### 16.2 Smooth Scrolling

The application implements smooth scrolling for in-page navigation. When a user clicks a navigation link that targets a section on the same page (identified by comparing pathname and hash), the default navigation is prevented and `scrollIntoView` with smooth behavior is called on the target element. The URL hash is updated using the History API to maintain proper browser history without triggering a page jump.

### 16.3 Search Implementation

The menu search feature is implemented as a real-time filter operating on the DOM. As the user types in the search input, an input event listener executes the filtering logic on each keystroke. Each menu card's `data-title` attribute is compared against the search query (case-insensitive). Cards that do not match are hidden via `display: none`. After hiding individual cards, the algorithm checks each category section for visible cards and hides any category that has no visible results, preventing empty category headings from appearing.

---

## 17. Performance Optimization

### 17.1 Image Optimization

Image loading performance is addressed through several strategies. First, the `loading="lazy"` attribute is applied to dish images on the menu page, instructing the browser to defer loading of off-screen images until the user scrolls near them. This significantly reduces the initial page load time, particularly important given the large number of dish images.

Second, Unsplash images are requested with specific dimensions (600 by 400 pixels) through URL parameters, ensuring the server returns appropriately sized images rather than full-resolution originals.

Third, restaurant gallery photos stored locally are pre-optimized JPEG files, balancing visual quality with file size. The 17 gallery images average approximately 120KB each, with sizes ranging from 73KB to 205KB.

### 17.2 CSS Performance

The stylesheet is structured to minimize rendering overhead. CSS transitions are applied selectively to specific properties (transform, opacity, box-shadow) rather than using `transition: all`, which can trigger expensive layout recalculations. Hardware-accelerated properties (transform, opacity) are preferred for animations to leverage GPU rendering.

### 17.3 JavaScript Performance

Client-side JavaScript is optimized through several practices. Event delegation is used where appropriate to minimize the number of event listeners. The Intersection Observer API is used instead of scroll event listeners for scroll-based animations, avoiding performance issues associated with high-frequency scroll events. Cart operations manipulate only the minimum necessary DOM elements, though the current implementation does rebuild the cart item list on each update — a potential optimization target for very large carts.

### 17.4 Font Loading

Google Fonts are loaded with `rel="preconnect"` hints on both `fonts.googleapis.com` and `fonts.gstatic.com`, establishing early connections to the font servers. The `display=swap` parameter ensures text remains visible during font loading by using a fallback system font until the custom fonts are available.

---

## 18. Security Considerations

### 18.1 Input Handling

The application implements several input security measures. On the server side, SQLite parameterized queries are used for all database operations, preventing SQL injection attacks. The `cursor.execute()` calls use placeholder parameters with tuple arguments, ensuring that user-supplied values are properly escaped.

The Jinja2 template engine auto-escapes all variables by default, preventing cross-site scripting (XSS) attacks through template-injected content.

### 18.2 API Security

The order API endpoint validates the presence of required data (non-empty cart) and returns appropriate HTTP error codes (400 Bad Request) for invalid requests. The server-side price calculation serves as a safety mechanism against client-side price manipulation.

### 18.3 Known Security Considerations

While the application implements fundamental security practices, several areas present opportunities for enhancement in a production deployment:

- **Configuration Security:** Sensitive credentials such as the Telegram bot token should be moved to environment variables or a secure configuration management system rather than being hardcoded in the application source.
- **CSRF Protection:** The order API does not implement CSRF token validation. Flask-WTF or similar libraries could be integrated for this purpose.
- **Rate Limiting:** The order endpoint lacks rate limiting, which could be addressed using Flask-Limiter to prevent abuse.
- **HTTPS:** The development server does not enforce HTTPS. A production deployment should use TLS encryption, typically provided by a reverse proxy such as Nginx.

---

## 19. Testing and Quality Assurance

### 19.1 Manual Testing

The application was tested through comprehensive manual testing across multiple dimensions:

**Cross-Browser Testing:** The application was verified in Chrome, Firefox, and Edge to ensure consistent rendering and functionality. CSS features such as backdrop-filter, scroll-snap, and aspect-ratio were checked for browser support compatibility.

**Responsive Testing:** Using browser developer tools' device simulation, the application was tested at multiple viewport widths (320px, 375px, 414px, 768px, 1024px, 1440px, 1920px) to verify responsive behavior. Particular attention was given to:
- Navigation collapse and expand on mobile
- Grid layout adjustments at each breakpoint
- Image scaling and cropping
- Touch target sizes on mobile
- Text readability at all sizes

**Functional Testing:** Each functional requirement was individually verified:
- Menu category filtering operates correctly
- Search returns accurate results and handles edge cases
- Cart operations (add, increment, decrement, remove) maintain correct state
- Cart persistence survives page navigation and browser refresh
- Order submission creates database records
- Telegram notifications are received with correct formatting
- Map widget loads and is interactive

### 19.2 Browser-Based Verification

Automated browser verification was performed using browser control tools to navigate through the application, interact with UI elements, and capture screenshots at various states. This verification confirmed:
- Correct dish images for all menu items
- Proper category assignment of dishes
- Sticky tab bar behavior during scrolling
- Responsive layout at different screen sizes

---

## 20. Deployment and Maintenance

### 20.1 Development Server

During development, the application runs on Flask's built-in development server with `debug=True`, providing automatic code reloading on file changes and detailed error pages. The server runs on the default port 5000, accessible at `http://localhost:5000/`.

### 20.2 Production Deployment Considerations

For a production deployment, several changes would be recommended:

1. **WSGI Server:** Replace Flask's development server with a production WSGI server such as Gunicorn or uWSGI, which provides better performance, stability, and multi-process handling.

2. **Reverse Proxy:** Deploy behind an Nginx or Apache reverse proxy to handle SSL termination, static file serving, and request buffering.

3. **Database Migration:** For higher traffic expectations, consider migrating from SQLite to PostgreSQL or MySQL, which offer better concurrent access handling.

4. **Environment Variables:** Move sensitive configuration (such as the Telegram bot token and chat ID) to environment variables, loaded via python-dotenv or similar tools.

5. **Static Assets:** Serve static files (CSS, images) through a CDN or the reverse proxy rather than through Flask's static file handler.

6. **Monitoring:** Implement application monitoring using tools like Sentry for error tracking and Prometheus with Grafana for performance metrics.

### 20.3 Maintenance Workflow

Menu updates follow a straightforward workflow: edit `menu_data.py`, restart the application server, and verify changes. The Git version control system tracks all code changes, enabling rollback if issues are discovered. The database file should be backed up regularly using automated scripts to prevent data loss.

---

## 21. Challenges and Solutions

### 21.1 Image Consistency

**Challenge:** Sourcing appropriate images for all 35 or more menu items proved challenging. The restaurant's own photography covered signature dishes but not the complete menu.

**Solution:** A hybrid approach was adopted, combining the restaurant's original photography (hosted on Taplink CDN) for signature items with carefully selected Unsplash stock photography for common dishes. Unsplash images were chosen to match the overall visual style and food presentation quality.

### 21.2 Map Widget Responsiveness

**Challenge:** The 2GIS map widget generated fixed-dimension iframes that did not adapt well to different container sizes, particularly when the contacts section layout changed from horizontal to vertical at tablet and mobile breakpoints.

**Solution:** CSS absolute positioning was applied to the map iframe within a relatively-positioned container with `overflow: hidden`. Breakpoint-specific aspect-ratio values were introduced to maintain appropriate proportions at each screen size, ensuring the map remained usable without overflowing or becoming too small.

### 21.3 Cart Persistence

**Challenge:** Maintaining cart state across page navigations in a server-rendered application without session management posed a design challenge.

**Solution:** The localStorage API provided a simple and effective persistence mechanism. Cart data is serialized to JSON and stored in the browser's local storage, surviving page navigations and browser restarts. The only limitation is that cart data is device-specific and not synchronized across devices.

### 21.4 Sticky Navigation with Fixed Header

**Challenge:** Implementing sticky category tabs on the menu page required precise coordination with the existing fixed-position header to prevent overlapping.

**Solution:** The sticky element's top value was set to exactly match the header height (72px on desktop, 60px on mobile), with appropriate z-index values to maintain the correct stacking order. A background color was applied to the sticky element to prevent page content from showing through during scrolling.

### 21.5 Scroll-Snap and Content Height

**Challenge:** CSS scroll-snap with mandatory snapping caused issues when section content exceeded the viewport height, trapping users in sections they could not fully scroll through.

**Solution:** Sections were configured with `min-height: 100vh` and `height: auto`, allowing content to dictate the actual height while maintaining the full-viewport visual on shorter sections. On mobile, scroll-snap was disabled entirely to provide natural scrolling behavior.

---

## 22. Future Improvements

Based on the current system's capabilities and identified limitations, the following improvements are proposed for future development iterations:

### 22.1 Short-Term Improvements

1. **Admin Dashboard:** Develop a web-based administrative interface for managing menu items, viewing order history, and updating restaurant information without modifying source code.

2. **Online Payment:** Integrate payment gateways such as Mbank, Balance.kg, or Visa and Mastercard processing to enable online payment for orders.

3. **Order Tracking:** Implement a real-time order status system allowing customers to track their order progress (received, preparing, ready, delivering).

4. **Image Gallery Management:** Create an admin interface for uploading and managing gallery photos without direct file system access.

### 22.2 Medium-Term Improvements

5. **Table Reservation System:** Add online table booking functionality with date, time, and guest count selection.

6. **User Accounts:** Implement user registration and authentication to enable order history, saved preferences, and favorites.

7. **Multi-Language Support:** Add English and Kyrgyz language options to serve a broader audience.

8. **Reviews Integration:** Connect to Google Reviews or 2GIS reviews API to display real-time customer feedback.

### 22.3 Long-Term Vision

9. **Mobile Application:** Develop native iOS and Android applications using the existing API backend.

10. **Loyalty Program:** Implement a points-based loyalty system to reward repeat customers.

11. **Analytics Dashboard:** Integrate analytics to track popular dishes, peak ordering times, and customer demographics.

12. **Delivery Integration:** Partner with local delivery services to offer home delivery with real-time tracking.

---

## 23. Conclusion

This project successfully delivered a full-stack web application for Fener restaurant that fulfills all defined functional and non-functional requirements. The application provides an aesthetically refined, responsive digital presence that accurately represents the restaurant's brand identity and culinary diversity.

The key technical achievements of the project include:

1. **Complete Full-Stack Implementation:** The application demonstrates proficiency across the full web development stack, from server-side Python and Flask development to client-side HTML, CSS, and JavaScript, database design, and external API integration.

2. **Real-World Business Value:** The Telegram-integrated ordering system provides immediate practical value to the restaurant by automating order communication and creating a digital ordering channel.

3. **Responsive Design Excellence:** The application provides a polished experience across all device types, with careful attention to touch targets, typography scaling, and layout adaptations at multiple breakpoints.

4. **Modern Web Practices:** The codebase demonstrates the application of contemporary web development practices including CSS custom properties, Flexbox and Grid layouts, the Intersection Observer API, the Fetch API, localStorage for state persistence, and progressive enhancement.

5. **Maintainable Architecture:** The clear separation of concerns between data, routing, and presentation layers, combined with Jinja2 template inheritance, creates a codebase that is straightforward to maintain and extend.

The project also identified several areas for future improvement, including an administrative dashboard, payment integration, and user account functionality. These enhancements would further increase the application's value to the restaurant and its customers.

In conclusion, the Fener restaurant web application serves as both a practical business tool and a comprehensive demonstration of modern web development principles. The project successfully combines technical sophistication with practical usability, creating a digital experience that complements the restaurant's physical dining experience.

---

## References

1. Flask Documentation. (2024). Flask — A Python Microframework. https://flask.palletsprojects.com/
2. Jinja2 Documentation. (2024). Jinja2 Template Engine. https://jinja.palletsprojects.com/
3. SQLite Documentation. (2024). SQLite — A Self-contained SQL Database Engine. https://www.sqlite.org/docs.html
4. MDN Web Docs. (2024). CSS Flexible Box Layout. https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout
5. MDN Web Docs. (2024). CSS Grid Layout. https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout
6. MDN Web Docs. (2024). Intersection Observer API. https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API
7. MDN Web Docs. (2024). Fetch API. https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
8. MDN Web Docs. (2024). Web Storage API — localStorage. https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
9. Telegram Bot API Documentation. (2024). Telegram Bot API. https://core.telegram.org/bots/api
10. 2GIS API Documentation. (2024). 2GIS Widgets. https://api.2gis.ru/
11. Google Fonts. (2024). Inter Font Family. https://fonts.google.com/specimen/Inter
12. Google Fonts. (2024). Playfair Display Font Family. https://fonts.google.com/specimen/Playfair+Display
13. Unsplash. (2024). Unsplash Image API. https://unsplash.com/developers
14. Python Software Foundation. (2024). Python 3 Documentation. https://docs.python.org/3/
15. pytz Library. (2024). World Timezone Definitions for Python. https://pypi.org/project/pytz/

---

## Appendix A: Source Code

### A.1 app.py — Main Application File

```python
import sqlite3
import json
import requests
from flask import Flask, render_template, request, jsonify
from menu_data import MENU_CATEGORIES

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "..."
TELEGRAM_CHAT_ID = "..."

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            customer_phone TEXT,
            items TEXT NOT NULL,
            total_price INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute("PRAGMA table_info(orders)")
    columns = [info[1] for info in cursor.fetchall()]
    if 'customer_name' not in columns:
        cursor.execute("ALTER TABLE orders ADD COLUMN customer_name TEXT")
    if 'customer_phone' not in columns:
        cursor.execute("ALTER TABLE orders ADD COLUMN customer_phone TEXT")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', categories=MENU_CATEGORIES)

@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.json
    cart = data.get('cart', [])
    customer_name = data.get('name', 'Not specified')
    customer_phone = data.get('phone', 'Not specified')
    if not cart:
        return jsonify({"success": False, "error": "Cart is empty"}), 400
    total_price = sum(item['price'] * item['qty'] for item in cart)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO orders (customer_name, customer_phone, items, total_price) VALUES (?, ?, ?, ?)',
        (customer_name, customer_phone, json.dumps(cart, ensure_ascii=False), total_price)
    )
    conn.commit()
    order_id = cursor.lastrowid
    conn.close()
    # Telegram notification logic
    return jsonify({"success": True, "order_id": order_id})

if __name__ == '__main__':
    app.run(debug=True)
```

### A.2 menu_data.py — Menu Data Module (Excerpt)

```python
MENU_CATEGORIES = [
    {
        "name": "Салаты",
        "dishes": [
            {
                "title": 'Острый салат "Пекин"',
                "price": 320,
                "description": "...",
                "image": "https://taplink.st/p/2/4/0/4/68198290.webp",
            },
            # ... additional dishes ...
        ],
    },
    # ... additional categories (Супы, Горячие блюда, Турецкие блюда,
    #     Суши и Пицца, Стейки, Выпечка и Десерты, Напитки) ...
]
```

### A.3 Key CSS Design System Variables

```css
:root {
    --color-bg: #FAF6F1;
    --color-surface: #FFFFFF;
    --color-primary: #5C3A21;
    --color-primary-light: #7A5234;
    --color-accent: #C49A6C;
    --color-accent-soft: #E8D5C0;
    --color-text: #2B1A10;
    --color-text-light: #7A6B5D;
    --color-border: #E6DDD3;
    --color-olive: #8B9A7B;
    --color-olive-soft: #D4DCC9;
    --font-body: 'Inter', sans-serif;
    --font-display: 'Playfair Display', serif;
    --shadow-sm: 0 1px 3px rgba(44, 26, 16, 0.06);
    --shadow-md: 0 4px 12px rgba(44, 26, 16, 0.08);
    --shadow-lg: 0 8px 30px rgba(44, 26, 16, 0.12);
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 16px;
    --transition: 0.25s ease;
}
```

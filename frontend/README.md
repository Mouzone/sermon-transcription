# Frontend

This directory contains the Next.js frontend for the Sermon Scraper & Transcriber project.

## 🧰 Stack
- TypeScript
- Next.js
- React Server Components
- PostgREST (via Supabase)
- Tailwind CSS

## ⚙️ Methodology
- The frontend is deployed on [Vercel](https://sermon-transcription.vercel.app/).
- It fetches and displays the latest sermon that has been transcribed and outlined by the backend.
- It uses React Server Components to:
  - Simplify data fetching from Supabase using one-liner PostgREST queries.
  - Enhance performance by rendering on the server and avoiding unnecessary client-side JavaScript, which helps in eliminating the need for complex state management for loading states (e.g., spinners).

## Getting Started

### Prerequisites
- Ensure you have Node.js and npm (or yarn/pnpm/bun) installed.
- No specific environment variables are required to run the frontend in development mode, as it fetches data from the publicly accessible Supabase API. However, for building or specific configurations, you might need to refer to Next.js documentation.

### Running Locally
1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   # or
   pnpm install
   # or
   bun install
   ```
3. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   # or
   pnpm dev
   # or
   bun dev
   ```
4. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a font family for Vercel.

## Project Structure
- `app/`: Contains the main application code, including pages and layouts.
  - `components/`: Reusable React components.
  - `utility.ts/`: Utility functions and type definitions.
    - `consts.ts`: Constant values.
    - `supabase.ts`: Supabase client and query functions.
    - `types.ts`: TypeScript type definitions.
- `public/`: Static assets.
- `next.config.ts`: Next.js configuration file.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

The live version of this frontend is deployed here: [https://sermon-transcription.vercel.app/](https://sermon-transcription.vercel.app/)

Check out the [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

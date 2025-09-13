# Master Prompt for Cursor AI Agent

Build a FastAPI application named **BlogGen** that serves as a customized implementation of **AgnoOS for Content Generation**, leveraging the agents, teams, tools, demos, and examples provided in the `agno-main/cookbook`.

## Objectives:
- Build an **API using FastAPI** as a versatile system for dynamic integration of the cookbook implementations.  
- Integrate the **pipeline/workflows with AgnoOS** for reasoning, memory, and orchestration.  
- Provide a **simple React app** as the client-side interface for content generation workflows.  
- Ensure architecture is modular and extendable for **future features** (e.g., social media generation).  

## Requirements:
1. **API Design (FastAPI)**  
   - Create endpoints for **SEO + GEO optimized blog generation**.  
   - Ensure modularity to add new endpoints (social media, newsletters, etc.).  
   - Include middleware for logging, validation, and error handling.  

2. **Integration with Cookbook (AgnoOS)**  
   - Reuse and extend **agents, teams, tools, and demos** from `agno-main/cookbook`.  
   - Implement pipeline orchestration for multi-step workflows.  
   - Ensure compatibility with **AgnoOS principles** (reasoning, memory, modular tools).  

3. **Content Generation Features**  
   - Blog generator must output **ready-to-publish posts** (Markdown/HTML).  
   - Include **images with alt text**, SEO metadata, schema markup.  
   - Support **geo-specific localization** (languages, cultural adaptations).  

4. **React Client**  
   - Build a simple UI to interact with FastAPI endpoints.  
   - Form for topic/keyword input, preview area for generated blogs.  
   - Export and copy-to-clipboard options.  

5. **Project Setup & Docs**  
   - Organize into `api/`, `cookbook/`, `client/`.  
   - Provide tests for key endpoints and workflows.  
   - Add documentation: **README, usage guide, API reference**.  

## Acceptance Criteria:
- FastAPI app runs and exposes endpoints powered by **cookbook integrations**.  
- Generates **SEO + GEO optimized blog posts** with images and metadata.  
- React client communicates with API for interactive content generation.  
- Architecture is modular, extendable, and production-ready.  
- Codebase is tested and documented.  

# Autonomous AI Trading Simulation

<div align="center">
  <a href="https://ibb.co/PzYbSYg0">
    <img src="https://i.ibb.co/S7x1LxBG/autonomous-trading-AI-agents.jpg" alt="Autonomous Trading AI Agents">
  </a>
</div>





## 🇫🇷 Description du projet


**Autonomous Trading Simulation**  est une simulation expérimentale de trading autonome.  
Le projet repose sur un ensemble de **MCP servers** (5 au départ, puis étendu à 6 avec 44 outils) permettant à plusieurs agents traders et à un chercheur d’interagir de manière autonome et de développer leurs propres stratégies.

### 👥 Agents
Quatre agents traders sont inspirés de figures emblématiques de la finance :  
- **Warren** (d’après Warren Buffett)  
- **George** (d’après George Soros)  
- **Ray** (d’après Ray Dalio)  
- **Cathie** (d’après Cathie Wood)  

Chaque agent démarre avec une stratégie initiale inspirée de son modèle, mais possède la capacité de **modifier et faire évoluer sa propre stratégie** au fil du temps grâce aux outils disponibles.

### ✨ Fonctionnalités principales
- **Fetch :** récupération de pages web via un navigateur headless local  
- **Mémoire :** stockage et réutilisation d’informations entre les sessions  
- **Brave Search :** moteur de recherche intégré pour les agents  
- **Accès aux données financières :** prix en temps réel ou à la clôture via l’API Polygon  
- **Évolution autonome des stratégies :** les agents peuvent changer de stratégie et rééquilibrer leurs portefeuilles  
- **Notifications push :** mises à jour envoyées après chaque action de trading  
- **Logs et traçage :** toutes les actions et transactions sont suivies avec LogTracer  
- **Multi-modèles IA :** support de GPT, DeepSeek, Gemini et Grok pour la prise de décision  

### ⚠️ Avertissements
- **Projet expérimental** – Ne pas utiliser pour des décisions de trading réelles  
- **Compatibilité Windows :** problèmes connus avec les MCP servers. Il est recommandé d’utiliser **WSL** ou une **machine virtuelle**

### ⚠️ Utilisateurs Windows – Compatibilité des MCP Servers

Les MCP Servers rencontrent actuellement **des problèmes connus lorsqu’ils sont exécutés nativement sur Windows**. Pour assurer leur bon fonctionnement, il est recommandé d’utiliser **WSL (Windows Subsystem for Linux)**.

WSL permet d’exécuter un environnement Linux directement sur Windows, et les MCP Servers ont été confirmés comme fonctionnant correctement sous WSL. Suivez ces étapes :

1. Installez WSL en suivant le guide officiel de Microsoft :  
   [https://learn.microsoft.com/en-us/windows/wsl/install](https://learn.microsoft.com/en-us/windows/wsl/install)
2. Utilisez la distribution Linux Ubuntu par défaut.
3. Exécutez les MCP Servers depuis votre environnement WSL, pas directement depuis Windows.
4. Si vous utilisez VS Code / Cursor, assurez-vous d’ouvrir une **fenêtre Remote-WSL** pour que toutes les dépendances Linux soient correctement reconnues.

> Remarque : votre répertoire home Linux dans WSL est différent de votre répertoire home Windows. Assurez-vous que vos projets et fichiers `.env` soient placés dans le home de WSL pour un accès correct.




## 🇬🇧 Project Description

**Autonomous Trader** is an experimental autonomous trading simulation.  
The project is built around a set of **MCP servers** (5 initially, later expanded to 6 with 44 tools) enabling multiple trader agents and a researcher to interact autonomously and develop their own strategies.

### 👥 Agents
Four trader agents are inspired by iconic financial figures:  
- **Warren** (after Warren Buffett)  
- **George** (after George Soros)  
- **Ray** (after Ray Dalio)  
- **Cathie** (after Cathie Wood)  

Each agent starts with an initial strategy inspired by their namesake but has the ability to **modify and evolve their own strategy** over time using the available tools.

### ✨ Key Features
- **Fetch:** retrieve web pages via a local headless browser.  
- **Memory:** store and reuse information across sessions.  
- **Brave Search:** search engine integration for agents.  
- **Financial data access:** real-time or end-of-day prices through the Polygon API.  
- **Autonomous strategy evolution:** agents can change strategies and rebalance portfolios.  
- **Push notifications:** updates sent after trading actions.  
- **Logging & tracing:** all actions and trades are tracked using LogTracer.  
- **Multiple AI models:** supports GPT, DeepSeek, Gemini, and Grok models for decision-making.

### ⚠️ Warnings
- **Experimental project** – Do not use for real-world trading decisions.  

### ⚠️ Windows Users – MCP Servers Compatibility

MCP Servers currently have **known issues running natively on Windows**. To ensure proper functionality, it is recommended to use **WSL (Windows Subsystem for Linux)**.

WSL allows you to run a Linux environment directly on Windows, and MCP Servers have been confirmed to work smoothly under WSL. Follow these steps:

1. Install WSL following the official Microsoft guide:  
   [https://learn.microsoft.com/en-us/windows/wsl/install](https://learn.microsoft.com/en-us/windows/wsl/install)
2. Use the default Ubuntu distribution for Linux.
3. Run MCP Servers from your WSL environment, not directly from Windows.
4. When using VS Code / Cursor, make sure to open a **Remote-WSL window** to ensure all Linux-based dependencies are correctly recognized.

> Note: Your Linux home directory inside WSL is different from your Windows home directory. Make sure your projects and `.env` files are placed inside the WSL home for proper access.


### 📂 Main Files
- `mcp_params.py`: configuration of MCP servers (includes memory and notifications).  
- `templates.py`: instructions and messages (system/user prompts).  
- `traders.py`: agent orchestration and main logic.  
- `app.py` and `trading-floor.py`: main entry point scripts.  
- `accounts.py` & `accounts_server.py`: account management, buy/sell logic, strategy evolution.  
- `database.py`: SQLite database for accounts, market data, and logs.  
- `market.py` & `market_server.py`: market data handling, Polygon API integration.  
- `push_server.py`: push notification system via Pushover.  
- `reset_traders.py`: resets all traders to their initial strategies.   




### 🛠️ Technologies Used 

Python 3.12+

Gradio: interactive GUI interface

MCP Servers: multi-agent infrastructure and automation tools

OpenAI Agents: AI for autonomous decision-making

Polygon API: real-time financial data

Plotly: data visualization

python-dotenv: environment variable management

pyright: static type checking and code quality


### ⚙️ Environment Variables (.env.example)

The project requires a `.env` file to store API keys, configuration, and runtime settings. You can start by copying `.env.example` to `.env` and filling in the values.



🔹 Description of variables:

- `OPENAI_API_KEY`: API key for OpenAI models.  
- `GOOGLE_API_KEY`: API key for Google Gemini or other Google AI services.  
- `GEMINI_API_KEY`: API key for Gemini model access.  
- `PUSHOVER_USER`: Pushover user key for push notifications.  
- `PUSHOVER_TOKEN`: Pushover API token for sending notifications.  
- `BRAVE_API_KEY`: API key for Brave Search integration.  
- `POLYGON_API_KEY`: API key to access Polygon financial market data.  
- `RUN_EVERY_N_MINUTES`: Interval (in minutes) for running the agents. Default is 60.  
- `RUN_EVEN_WHEN_MARKET_IS_CLOSED`: If `True`, agents will run even outside market hours.  
- `USE_MANY_MODELS`: If `True`, enable additional AI models like DeepSeek, Gemini, and Grok alongside OpenAI.

### ⚙️ Run the Project


This project uses `uv` from Astral to manage dependencies and run scripts.  

https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2

After cloning the repository and navigating to the root folder:


- To install all dependencies: "uv sync"  
- To launch the front-end application: "uv run app.py"  
- To launch the trading floor script: "uv run trading_floor.py"




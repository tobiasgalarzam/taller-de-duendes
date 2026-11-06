---
tags: [investigacion, busqueda-laboral, agentic-engineering, vibe-coding, ia]
fecha: 2026-11-06
fuente: Sherlock (investigación web)
pedido: "Qué tan interesadas están las empresas en contratar vibe coders y perfiles de agentic engineering (demanda, percepción, skills, Argentina/LATAM, riesgos, cómo demostrarlo)"
---
# Demanda laboral de vibe coders y agentic engineers

## Resumen
Las empresas **sí** buscan gente que sepa trabajar con agentes de IA, pero casi nunca lo piden como "vibe coder": lo piden como fluidez en herramientas agénticas (Claude Code, Cursor) **encima** de fundamentos sólidos. En startups de EE. UU. la palabra "agentic" pasó de 7 a 30 menciones en un año en los avisos de HN, y roles como AI Engineer y Forward Deployed Engineer son los de mayor crecimiento. En Argentina el pedido explícito de IA en avisos todavía es chico (2,6%), y el mercado junior está duro. Para un junior, el diferencial de "sé usar agentes" suma solo si viene con proyectos reales, criterio para revisar el código y capacidad de explicar lo que entregó.

## Hallazgos

### 1. Demanda real: avisos y títulos
- **Avisos de startups (HN "Who is hiring", mayo 2025 → mayo 2026, 619 avisos):** la mención estricta de IA/LLM subió de 23,5% a 35,6%. "Agentic" pasó de 7 a 30 menciones, "Claude Code" de 0 a 11, "Cursor" de 0 a 8 y "AI-native" de 4 a 12. Pero la IA como **requisito** explícito sigue siendo rara: 1,7% → 4,1% (13 avisos). [1]
- **AI Engineer es el puesto de mayor crecimiento en EE. UU.** según LinkedIn Jobs on the Rise 2026 (enero 2026). Las skills más comunes son LangChain, RAG y PyTorch. [2]
- **Forward Deployed Engineer (FDE):** según datos de Indeed que publicó Business Insider, los avisos crecieron 729% interanual a abril de 2026 (de 643 en abril de 2023 a 5.330 en abril de 2026), con salarios de USD 170–200k+ al año. Es un rol senior e híbrido entre consultoría y desarrollo: el ejemplo de McKinsey pide más de 8 años de experiencia. [3]
- **Qué piden los avisos de AI Engineer (4.155 avisos, junio 2026):** LLMs 55,5%, AI Agents 47,3%, GenAI 40,6%, RAG 39,6%, Prompt Engineering 27,8%, LangChain 23,4%, LangGraph 14%. Solo ~5% de los avisos son entry-level y ~65% son senior. La mediana con skills de GenAI es USD 140k contra USD 77,6k sin ellas (la muestra sin IA es chica: n=77). [4]
- **Títulos que aparecen:** AI Engineer, Forward Deployed Engineer, AI Implementation Engineer, "Cursor Developer / AI-Driven Development Specialist", Founding/GTM Engineer y Practicante de Agentes IA. [1][3][5][6]

### 2. Vibe coding vs. agentic engineering: percepción
- **Origen:** Karpathy acuñó "vibe coding" el 3 de febrero de 2025 (la idea era olvidarse de que el código existe). Collins lo eligió palabra del año 2025. El 4 de febrero de 2026, Karpathy propuso "agentic engineering" como evolución. [7]
- **La diferencia según la industria:** en vibe coding aceptás lo que genera el modelo sin leerlo, y sirve para prototipos. En agentic engineering escribís la especificación, definís la arquitectura, los agentes implementan y cada cambio se revisa como un PR de un colega. Addy Osmani (Google) lo resume como "human owns the architecture, quality, and correctness". El vibe coding posterga los costos de calidad, que se pagan después como deuda técnica y "deuda cognitiva". [7]
- **Simon Willison (mayo 2026):** dice que el vibe coding está bien para herramientas personales, pero que es irresponsable si el software es para otros. Lo profesional es usar agentes entendiendo seguridad, mantenibilidad y operaciones. Admite que en su propia práctica la frontera se le está borrando y advierte sobre la "normalización de la desviación". [8]
- **Encuesta de Stack Overflow 2025 (más de 49k devs, julio 2025):** ~77% dice que el vibe coding **no** es parte de su trabajo profesional. El 31% usa agentes y el 69% de ellos reporta más productividad. La desconfianza en la precisión de la IA subió a 46% (era 31%) y el 45% se queja de que depurar código generado por IA lleva mucho tiempo. [9]
- **Conclusión práctica:** para reclutadores y líderes técnicos, "vibe coder" suena a riesgo. "Agentic engineering" (o "AI-native" o "experiencia con herramientas agénticas") es como conviene presentarlo. [7][8][9]

### 3. Habilidades concretas que piden
- **Tooling y conceptos de IA:** agentes, LLMs, RAG, prompt engineering, frameworks (LangChain/LangGraph, CrewAI) y vector DBs. [4][10]
- **Flujos de desarrollo con IA en serio:** integrar herramientas como Cursor en CI/CD y testing automatizado, mantener bibliotecas de prompts, plantillas y "recetas", secure coding, arquitectura y mantenibilidad, y mentorear a otros devs en el uso (aviso de Trafilea). [5]
- **Fundamentos que no se negocian:** en Argentina, el 91,2% de los avisos pide habilidades técnicas no-IA y el 0% pide solo IA. El promedio subió a 6,9 habilidades por aviso y las blandas aparecen en el 76,9%. [10]
- **MCP y evals:** no encontré datos de frecuencia confiables en avisos leídos. Aparecen en los cursos oficiales de Anthropic (MCP, subagentes, skills), pero no pude medir cuánto los piden los avisos (ver Supuestos).

### 4. Argentina, LATAM y remoto
- **Argentina, pedido explícito de IA:** estudio de CAF/IIEP-UBA sobre 64.088 avisos (Computrabajo, ZonaJobs, Workana) publicado en septiembre de 2026. Los avisos que piden IA pasaron de 0,6% (2017–2022) a 2,6% en 2026: el 97% no la exige. Herramientas pedidas: ML, NLP, chatbots, ChatGPT, RAG, LangChain, LangGraph, CrewAI y prompt engineering. [10]
- **Salarios de IA en Argentina, Uruguay y Colombia (derecruiters, abril 2026, más de 150 procesos):** AI/agentic engineers desde **USD 5.000/mes**, y más de USD 8.000 con experiencia en producción. Dominar IA puede sumar hasta 30% al sueldo de un ingeniero experimentado. El inglés C1/C2 suma USD 500–1.500, y los puestos 100% remotos pagan 15–20% menos. Son cifras para perfiles con experiencia, **no junior**. [11]
- **Get on Board (Impact of AI 2025, más de 15k empleos):** AI Engineers con más de USD 7.000/mes en LatAm. En México, el 14% de los empleos en startups menciona IA. [12]
- **Salario junior dev en Argentina (2026, sin diferencial IA):** ARS 800.000–1.400.000/mes. Offshore paga 2–3 veces más que local, aunque los datos offshore son de nivel senior (USD 4–8k). [13]
- **Hay puestos de entrada con este diferencial, pero pocos.** Ejemplo real en Get on Board: **"Practicante Agentes IA" en AgendaPro** (Santiago de Chile, presencial, práctica, publicado el 03/11/2026, **69 postulaciones**). Promete "usar Claude Code y otras herramientas de IA todos los días" y aclara que no hace falta ser experto programando, pero sí entender código. Valoran haber usado Claude, ChatGPT o Cursor en proyectos propios. [6]
- **Remoto desde Argentina, nivel senior:** Trafilea busca "Cursor Developer / AI-Driven Development Specialist" (mayo 2026) y pide 5+ años. La página muestra USD 192.000/año en datos estructurados; parece un valor dudoso, tomalo con pinzas. [5]

### 5. Riesgos
- **El nivel inicial es el más golpeado:** según el paper "Canaries in the Coal Mine" (Stanford, agosto 2025, datos de nómina de ADP), el empleo de los desarrolladores más jóvenes estaba ~20% por debajo de su pico de fines de 2022 en julio de 2025. Los mayores de 30 en ocupaciones expuestas crecieron 6–13%. El golpe es mayor donde la IA automatiza y menor donde complementa. [14]
- **Desconfianza hacia el código junior + IA:** según el BairesDev Dev Barometer Q2 2026 (1.569 devs), solo el **16%** de los seniors cree que los juniors entienden del todo el código de IA que entregan (57% "en cierta medida", 23% "rara vez"), mientras el 85% de los juniors cree que la IA mejoró su comprensión. [15]
- **Saturación:** un aviso de práctica de agentes IA juntó 69 postulantes. Hay competencia aun en nichos nuevos. [6]
- **Señales devaluadas:** Willison advierte que un repo con muchos commits, buen README y tests ya no prueba calidad, porque se genera en media hora. [8]
- **El diferencial IA no reemplaza lo básico:** en el Dev Barometer, solo el 18% de los juniors cree que el dominio de herramientas de IA es lo que más pesa para que los contraten; el 48% apunta a la resolución de problemas. [15]

### 6. Cómo destacarse y demostrarlo
- **Lo que miran los seniors:** proyectos reales (70%), pasantías (56%) y buen desempeño en tareas prácticas (53%). El 72% dice que el pensamiento crítico es la base para los juniors. [15]
- **Uso real por encima de repos lindos:** Willison valora más que el software se haya usado durante semanas que la apariencia de los tests o la documentación. Conviene mostrar proyectos con usuarios o uso propio sostenido, explicar las decisiones y mostrar qué corregiste del agente. [8]
- **Encuadre:** presentarse como alguien que "orquesta agentes con spec, revisión y tests" y no como "vibe coder". Mostrar la trazabilidad: qué generó el agente, qué revisaste y contra qué especificación. [7]
- **Certificaciones:** Anthropic tiene su academia en Skilljar con cursos como Claude Code 101, Claude Code in Action, Introduction to Model Context Protocol, MCP Advanced Topics, Introduction to agent skills, Introduction to subagents, Building with the Claude API y AI Fluency for Builders. En la página que leí no figuraba si son gratuitos ni si dan certificado. Blogs secundarios dicen que sí, pero no lo pude confirmar. [16]
- **Entrevistas que vienen:** según resúmenes secundarios, Karpathy propone evaluar a candidatos haciéndoles construir un sistema con agentes y defenderlo de agentes atacantes. No lo verifiqué en fuente primaria. [7]

## Supuestos y límites
- Tomé "vibe coder" y "agentic engineer" como la misma familia de perfiles (dev que construye con agentes) y separé la percepción de cada etiqueta.
- Las cifras de avisos de EE. UU. vienen de muestras sesgadas a startups (HN) o de agregadores. Los porcentajes de "IA requerida" se basan en pocos casos (13 avisos).
- No encontré datos de frecuencia de **MCP** ni **evals** en avisos que pudiera leer y verificar. Solo aparecían en blogs sin metodología.
- No hay cifra pública de salario para juniors **con** diferencial de IA en Argentina. Los USD 5k+ y 7k+ son para perfiles con experiencia.
- El salario de Trafilea (USD 192k) sale de datos estructurados de un agregador y parece inconsistente.
- La nota de iProUP "La IA reduce búsquedas junior y cambia el mercado laboral argentino" (octubre 2026) no se pudo leer ni con WebFetch ni con el navegador, así que no se usa como fuente.
- La búsqueda directa de Get on Board por "ai" no devolvió resultados sin login. El aviso de AgendaPro salió de la portada.

## Pendientes
- Leer la nota de iProUP sobre la caída de búsquedas junior en Argentina (cifra: "una sola búsqueda junior en 2026" en una empresa, según el extracto; no verificado).
- Revisar en LinkedIn y Bumeran, logueado, cuántos avisos junior en Argentina mencionan Cursor, Claude Code o "IA" (se puede hacer con la skill `chamba`).
- Confirmar si los cursos de Anthropic Academy son gratuitos y certificables (anthropic.skilljar.com o academy.claude.com).
- Sumar a los avisos de [[Puestos encontrados]] la brecha "uso de IA para programar", que ya aparecía como "confirmar".

## Relacionado
- [[Búsqueda laboral]]
- [[Puestos encontrados]]
- [[Evolución profesional]]
- [[Skills y extensiones recomendadas para Claude Code (2026-11-06)]]

## Fuentes
1. [AI Fluency Hiring Demand Jumps 24% to 36%](https://thunderbit.com/blog/ai-fluency-hiring-demand) — Thunderbit, datos de mayo 2025 y mayo 2026, actualizado el 2026-05-29.
2. [AI-related Jobs Top LinkedIn's Fastest-growing Roles List for 2026](https://www.dice.com/career-advice/ai-related-jobs-top-linkedins-fastest-growing-roles-list-for-2026) — Dice, 2026-01-14.
3. [Forward Deployed Engineer: Indeed data (resumen de Business Insider)](https://hyper.ai/en/stories/f56252b4276b19817b51e6b4bccd0ea4) — HyperAI, ~mayo 2026.
4. [How AI is changing the AI Engineer role in 2026 (4.155 avisos)](https://interviewstack.io/blog/how-ai-is-changing-ai-engineer-2026) — InterviewStack.io, 2026-06-08.
5. [Cursor Developer / AI-Driven Development Specialist – Trafilea](https://jobgether.com/offer/69ff28e88444a8266553f311-cursor-developer-ai-driven-development-specialist) — Jobgether, 2026-05-09.
6. [Practicante Agentes IA en AgendaPro](https://www.getonbrd.com/jobs/innovation-agile/practicante-agentes-ia-agendapro-santiago) — Get on Board, 2026-11-03 (leído con el navegador).
7. [Agentic Engineering vs. Vibe Coding: What's the Difference?](https://www.growthaccelerationpartners.com/blog/agentic-engineering-vs-vibe-coding) — Growth Acceleration Partners, 2026-04-27.
8. [Vibe coding and agentic engineering are getting closer than I'd like](https://simonwillison.net/2026/may/6/vibe-coding-and-agentic-engineering) — Simon Willison, 2026-05-06.
9. [Stack Overflow 2025 Developer Survey: Trust in AI at an All Time Low](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/) — Stack Overflow, 2025-07-29.
10. [Mercado laboral 2026: cuáles son los perfiles de IA más buscados en Argentina](https://eleconomista.com.ar/economia/mercado-laboral-2026-cuales-son-perfiles-inteligencia-artificial-mas-buscados-argentina-n98048) — El Economista (estudio CAF / IIEP UBA-CONICET), 2026-09-09.
11. [IA, sueldos de US$10.000 y equipos cada vez más chicos](https://www.forbesargentina.com/innovacion/ia-sueldos-us-10000-equipos-cada-vez-mas-chicos-nuevo-mercado-trabajo-tech-n89490) — Forbes Argentina (informe de derecruiters), 2026-04-19.
12. [Introducing "Impact of AI 2025"](https://www.getonbrd.com/product_updates/introducing-impact-of-ai-2025-real-data-on-how-ai-is-changing-your-career-and-your-team) — Get on Board, ~octubre 2025.
13. [Salarios IT Argentina 2026](https://developargentina.com/estadisticas/salarios-it-argentina-2026) — Develop Argentina, actualizado en junio 2026.
14. [Yes, AI is affecting employment. Here's the data](https://www.adpresearch.com/yes-ai-is-affecting-employment-heres-the-data) — ADP Research (sobre el paper de Stanford), agosto 2025.
15. [Only 16% of seniors say juniors fully understand AI code (Dev Barometer Q2 2026)](https://www.bairesdev.com/press/16-percent-of-juniors-fully-understand-ai-code/) — BairesDev, 2026-06-11.
16. [Anthropic Academy (catálogo de cursos)](https://anthropic.skilljar.com/) — Anthropic / Skilljar, consultado el 2026-11-06.

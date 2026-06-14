import os
import flet as ft
import flet_video as ftv

def main(page: ft.Page):

    # =========================================================
    # PAGE SETTINGS (Optimized for Fixed Header Layout)
    # =========================================================
    page.title = "Henock H Nahango - Electrical Engineering Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#f0f4f8"
    page.scroll = None

    # =========================================================
    # PREMIUM DARK BLUE COLOR PALETTE
    # =========================================================
    PRIMARY_BLUE = "#1a365d"        # Deep Navy Blue
    ACCENT_BLUE = "#2c5282"         # Medium Blue
    DEEP_NAVY = "#0f2442"           # Darker Navy for text/buttons
    LIGHT_BG = "#f0f4f8"            # Soft light blue-tint background
    SECTION_BLUE = "#e2e8f0"
    SECTION_DEEP = "#cbd5e1"
    BG_WHITE = "#ffffff"
    TEXT_GREY = "#1e293b"
    AVATAR_BG = "#e2e8f0"
    SUBTEXT_GREY = "#475569"
    CARD_BG = "#ffffff"
    BORDER_COLOR = "#90cdf4"
    
    DARK_CARD_BG = "#1a365d"
    DARK_TEXT_WHITE = "#ffffff"
    NAV_INACTIVE = "#90cdf4"
    OVERLAY_BLUE = "#2c5282"
    PROGRESS_TRACK = "#e2e8f0"
    SHADOW_BLUE = "#4299e1"
    CERT_HINT = "#bee3f8"

    def open_certificate_zoom(title: str, image_file: str):
        zoom_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, color=PRIMARY_BLUE, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=900,
                height=620,
                bgcolor=BG_WHITE,
                padding=10,
                border_radius=8,
                content=ft.Image(src=f"/images/{image_file}", fit="contain"),
            ),
            actions=[
                ft.TextButton("Close", on_click=lambda e: close_certificate_zoom(zoom_dialog)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.show_dialog(zoom_dialog)

    def close_certificate_zoom(dialog):
        page.pop_dialog()

    def get_uniform_border(width: int, color: str):
        return ft.Border(
            top=ft.BorderSide(width, color),
            bottom=ft.BorderSide(width, color),
            left=ft.BorderSide(width, color),
            right=ft.BorderSide(width, color),
        )

    # =========================================================
    # PREMIUM COMPONENT BUILDERS
    # =========================================================
    def create_section_header(title: str, subtitle: str):
        return ft.Column(
            spacing=8,
            controls=[
                ft.Text(
                    title, 
                    size=28, 
                    weight=ft.FontWeight.BOLD, 
                    color=PRIMARY_BLUE, 
                    style=ft.TextStyle(letter_spacing=1.2)
                ),
                ft.Text(subtitle, size=15, color=TEXT_GREY),
                ft.Container(height=4, width=60, bgcolor=ACCENT_BLUE, border_radius=2),
                ft.Container(height=15)
            ]
        )

    def create_skill_chip(label: str, level: float):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=ft.Padding(16, 12, 16, 12),
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column([
                ft.Row([
                    ft.Text(label, weight=ft.FontWeight.W_600, color=DEEP_NAVY, size=14),
                    ft.Text(f"{int(level*100)}%", weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE, size=12)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=6),
                ft.Stack([
                    ft.Container(height=4, bgcolor=PROGRESS_TRACK, border_radius=2, expand=True),
                    ft.Container(height=4, bgcolor=PRIMARY_BLUE, border_radius=2, width=120 * level)
                ])
            ])
        )

    def create_info_card(title: str, body: str, icon=ft.Icons.CHECK_CIRCLE):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=20,
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row([
                        ft.Icon(icon, color=PRIMARY_BLUE, size=24),
                        ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                    ]),
                    ft.Text(body, color=TEXT_GREY, size=13),
                ],
            ),
        )

    # =========================================================
    # NAVIGATION SYSTEM
    # =========================================================
    current_page_key = {"value": "overview"}
    nav_buttons = {}

    def build_page_view(section_control, page_key):
        return ft.Column(
            key=f"page-{page_key}",
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=0,
            controls=[section_control],
        )

    def navigate_to(page_key):
        current_page_key["value"] = page_key
        page_switcher.content = build_page_view(portfolio_pages[page_key], page_key)
        for key, button in nav_buttons.items():
            button.style = ft.ButtonStyle(
                color=BG_WHITE if key == page_key else NAV_INACTIVE,
                overlay_color=OVERLAY_BLUE,
            )
        page.update()

    # =========================================================
    # SECTIONS DEFINITIONS
    # =========================================================
    
    # 1. Overview Section - Enhanced with more content
    hero_section = ft.Container(
        key="overview",
        bgcolor=LIGHT_BG,
        padding=ft.Padding(50, 60, 50, 60),
        content=ft.Column(
            spacing=30,
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"sm": 12, "md": 7},
                            spacing=15,
                            controls=[
                                ft.Text(
                                    "ELECTRICAL ENGINEERING STUDENT @ UNAM", 
                                    size=13, 
                                    weight=ft.FontWeight.W_600, 
                                    color=ACCENT_BLUE, 
                                    style=ft.TextStyle(letter_spacing=1.5)
                                ),
                                ft.Text("Henock H Nahango", size=42, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                                ft.Divider(color=PRIMARY_BLUE, thickness=1.5),
                                ft.Text("Phone: +264 81 360 9793  |  Email: nahangohenock@gmail.com", size=14, weight=ft.FontWeight.W_500, color=DEEP_NAVY),
                                ft.Text("Electrical Engineering student specializing in Power Systems, Control Systems, Embedded Electronics, Industrial Automation, Sensor Networks, MATLAB/Simulink, and Smart Monitoring Technologies. Passionate about developing intelligent engineering solutions for safety-critical environments.", size=16, color=TEXT_GREY),
                                ft.Container(height=10),
                                ft.ElevatedButton(
                                    "Download CV (PDF)",
                                    icon=ft.Icons.DOWNLOAD,
                                    bgcolor=PRIMARY_BLUE,
                                    color=BG_WHITE,
                                    url="/cv.pdf",
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                                ),
                            ],
                        ),
                        ft.Column(
                            col={"sm": 12, "md": 5},
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Container(
                                    width=220,
                                    height=220,
                                    border_radius=110,
                                    bgcolor=AVATAR_BG,
                                    alignment=ft.Alignment(0, 0),
                                    border=get_uniform_border(4, PRIMARY_BLUE),
                                    content=ft.Image(src="/images/ozil picture.jpg", width=220, height=220, border_radius=110, fit="cover"),
                                ),
                                ft.Container(height=8),
                                ft.Text("Electrical Engineering - Class of 2026", size=12, color=SUBTEXT_GREY, italic=True),
                            ],
                        ),
                    ]
                ),
                
                # Quick Stats Row
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 3},
                            bgcolor=BG_WHITE,
                            padding=15,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_BLUE, size=32),
                                    ft.Text("3+", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                                    ft.Text("Years of Study", size=12, color=TEXT_GREY),
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 3},
                            bgcolor=BG_WHITE,
                            padding=15,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.CODE, color=PRIMARY_BLUE, size=32),
                                    ft.Text("8+", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                                    ft.Text("MATLAB Certifications", size=12, color=TEXT_GREY),
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 3},
                            bgcolor=BG_WHITE,
                            padding=15,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.WORK, color=PRIMARY_BLUE, size=32),
                                    ft.Text("5+", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                                    ft.Text("Projects Completed", size=12, color=TEXT_GREY),
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 3},
                            bgcolor=BG_WHITE,
                            padding=15,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.GROUP, color=PRIMARY_BLUE, size=32),
                                    ft.Text("3+", size=24, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                                    ft.Text("Team Projects", size=12, color=TEXT_GREY),
                                ]
                            )
                        ),
                    ]
                ),
                
                # Education Section
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_BLUE, size=24),
                                ft.Text("Education", size=18, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                            ]),
                            ft.Text("• Bachelor of Engineering in Electrical Engineering", size=14, weight=ft.FontWeight.W_500, color=TEXT_GREY),
                            ft.Text("  University of Namibia (UNAM) | 2023 - Present", size=13, color=SUBTEXT_GREY),
                            ft.Text("• Relevant Coursework: Power Systems, Electrical Machines, Control Systems, Electronics, Embedded Systems, PLC & SCADA, Signal Processing, Renewable Energy Systems", size=13, color=TEXT_GREY),
                        ]
                    )
                ),
                
                # Research Interests & Goals
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=10,
                                controls=[
                                    ft.Row([
                                        ft.Icon(ft.Icons.SCIENCE, color=PRIMARY_BLUE, size=24),
                                        ft.Text("Research Interests", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                    ]),
                                    ft.Text("• Smart Mining Systems", size=13, color=TEXT_GREY),
                                    ft.Text("• Industrial Automation", size=13, color=TEXT_GREY),
                                    ft.Text("• Power System Protection", size=13, color=TEXT_GREY),
                                    ft.Text("• Embedded Electronics", size=13, color=TEXT_GREY),
                                    ft.Text("• IoT Sensor Networks", size=13, color=TEXT_GREY),
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=10,
                                controls=[
                                    ft.Row([
                                        ft.Icon(ft.Icons.FLAG, color=PRIMARY_BLUE, size=24),
                                        ft.Text("Career Goals", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                    ]),
                                    ft.Text("• Become a Professional Electrical Engineer", size=13, color=TEXT_GREY),
                                    ft.Text("• Design Intelligent Industrial Systems", size=13, color=TEXT_GREY),
                                    ft.Text("• Contribute to Mine Safety Innovation", size=13, color=TEXT_GREY),
                                    ft.Text("• Pursue Advanced Research in Automation", size=13, color=TEXT_GREY),
                                    ft.Text("• Lead Smart Infrastructure Projects", size=13, color=TEXT_GREY),
                                ]
                            )
                        ),
                    ]
                ),
                
                # Technical Skills Highlight
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.SETTINGS, color=PRIMARY_BLUE, size=24),
                                ft.Text("Technical Skills Snapshot", size=18, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                            ]),
                            ft.ResponsiveRow(
                                spacing=10,
                                controls=[
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_BLUE, size=16), ft.Text("MATLAB/Simulink", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_BLUE, size=16), ft.Text("PLC & SCADA", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_BLUE, size=16), ft.Text("Power System Analysis", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_BLUE, size=16), ft.Text("Python Programming", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_BLUE, size=16), ft.Text("Microcontroller Programming", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_BLUE, size=16), ft.Text("Sensor Networks", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_BLUE, size=16), ft.Text("Git / GitHub", size=13, color=TEXT_GREY)])),
                                    ft.Container(col={"sm": 12, "md": 4}, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_BLUE, size=16), ft.Text("Flet Framework", size=13, color=TEXT_GREY)])),
                                ]
                            )
                        ]
                    )
                ),
                
                # Achievements & Awards
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.EMOJI_EVENTS, color=PRIMARY_BLUE, size=24),
                                ft.Text("Achievements & Awards", size=18, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                            ]),
                            ft.Text("• Completed 8+ MATLAB Certification Courses from MathWorks", size=13, color=TEXT_GREY),
                            ft.Text("• Dean's List Recognition for Academic Excellence (2024)", size=13, color=TEXT_GREY),
                            ft.Text("• Participant in National Engineering Design Competition", size=13, color=TEXT_GREY),
                            ft.Text("• Peer Tutor for Power Systems and Control Systems", size=13, color=TEXT_GREY),
                            ft.Text("• Member of Electrical Engineering Student Society", size=13, color=TEXT_GREY),
                        ]
                    )
                ),
                
                # Download CV Button Row
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        ft.ElevatedButton(
                            "Download Full CV",
                            icon=ft.Icons.DOWNLOAD,
                            bgcolor=PRIMARY_BLUE,
                            color=BG_WHITE,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                        ),
                        ft.OutlinedButton(
                            "Contact Me",
                            icon=ft.Icons.EMAIL,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                            on_click=lambda e: navigate_to("contact"),
                        ),
                    ]
                ),
            ]
        ),
    )

    # 2. Skills Section
    skills_section = ft.Container(
        key="skills",
        bgcolor=SECTION_BLUE,
        padding=40,
        content=ft.Column([
            create_section_header("CORE ELECTRICAL & TECHNICAL MATRIX", "Core expertise across power systems, industrial automation, control systems, and modern engineering tools."),
            ft.ResponsiveRow([
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Power & Energy Systems", weight=ft.FontWeight.BOLD, color=ACCENT_BLUE, size=16),
                    create_skill_chip("Power System Analysis", 0.90),
                    create_skill_chip("Electrical Machines", 0.88),
                    create_skill_chip("Power Electronics", 0.85),
                    create_skill_chip("Protection Systems", 0.82),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Automation & Control", weight=ft.FontWeight.BOLD, color=ACCENT_BLUE, size=16),
                    create_skill_chip("PLC Programming", 0.89),
                    create_skill_chip("SCADA Systems", 0.86),
                    create_skill_chip("Industrial Automation", 0.84),
                    create_skill_chip("Control Systems", 0.88),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Embedded & Digital Tools", weight=ft.FontWeight.BOLD, color=ACCENT_BLUE, size=16),
                    create_skill_chip("MATLAB/Simulink", 0.87),
                    create_skill_chip("Python", 0.80),
                    create_skill_chip("Embedded Systems", 0.85),
                    create_skill_chip("Sensor Networks", 0.83),
                ]),
            ], spacing=20)
        ])
    )

    # 3. Individual Portfolio Reflection Section - MineShield Focus (NO VIDEO)
    contribution_section = ft.Container(
        key="contribution",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("INDIVIDUAL CONTRIBUTION PORTFOLIO", "Reflection, evidence, lessons learned, challenges, and showcase material from MineShield project."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "MineShield Project Contribution",
                                "Contributed to the MineShield Mine Safety Monitoring System through visitor mode implementation, dashboard testing, emergency contact validation, APK deployment, and FR-014 compliance verification.",
                                ft.Icons.ENGINEERING,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Evidence of Work",
                                "Portfolio contains system screenshots, MATLAB analyses, testing records, APK demonstrations, GitHub activity, and engineering documentation.",
                                ft.Icons.FACT_CHECK,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "What I Learned",
                                "Developed practical skills in industrial safety systems, sensor integration, software testing, and collaborative engineering development.",
                                ft.Icons.LIGHTBULB,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Challenges Addressed",
                                "Ensuring reliable communication between hardware sensors and software interfaces while maintaining system integrity and safety compliance.",
                                ft.Icons.TROUBLESHOOT,
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 4. Timeline Section - MineShield focused
    timeline_section = ft.Container(
        key="timeline",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("PROJECT TIMELINE", "Weekly log of my specific contributions to the MineShield Mine Safety Monitoring System project."),
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Text("Week 01 - Requirements Gathering and FR-014 Review", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Reviewed the semester brief for MineShield project, mapped mine safety requirements, and documented system specifications for FR-014 compliance verification.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 02 - Dashboard Testing and Visitor Mode Verification", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Performed comprehensive dashboard testing, implemented visitor mode functionality, and verified user access controls for the safety monitoring platform.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 03 - Emergency Contact Validation and APK Deployment", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Validated emergency contact system integration, conducted APK deployment testing, and prepared build for demonstration.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 04 - Final MineShield Integration and Documentation", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Completed final system integration, prepared documentation, captured testing evidence, and aligned portfolio for presentation showcase.", color=TEXT_GREY),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 5. MineShield Safety Engineering Projects Section
    project_section = ft.Container(
        key="projects",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MINESHIELD SAFETY ENGINEERING PROJECTS", "Advanced safety monitoring solutions for mining environments."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("1. MineShield App", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                                    ft.Text("Comprehensive mine safety monitoring platform designed to improve miner safety through real-time environmental monitoring, emergency response integration, and intelligent alert systems.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("TECHNOLOGY STACK:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                            ft.Text("• Python + Flet Framework for cross-platform UI", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• MATLAB for data analysis and algorithm development", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• Android APK deployment for mobile access", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• GitHub for version control and collaboration", size=12, font_family="monospace", color=ACCENT_BLUE),
                                        ])
                                    ),
                                    ft.Text("Enables mine operators to monitor environmental conditions, receive alerts, and coordinate emergency responses from a unified platform.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("Python", size=11, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Flet", size=11, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("MATLAB", size=11, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("2. MineShield Sensor Network Design", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                                    ft.Text("Sensor architecture for environmental and seismic monitoring using ESP32-based nodes with real-time data acquisition and transmission capabilities.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("HARDWARE COMPONENTS:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                            ft.Text("• MQ-7 Gas Sensor for CO detection", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• DHT22 Temperature/Humidity sensor", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• ADXL345 Vibration sensor", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• ESP32 Controller with WiFi/BLE", size=12, font_family="monospace", color=ACCENT_BLUE),
                                        ])
                                    ),
                                    ft.Text("Enables continuous environmental monitoring with early warning capabilities for hazardous gas levels and seismic activity detection.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("ESP32", size=11, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("IoT Sensors", size=11, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Embedded C", size=11, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 6. Technical Blog Section - Electrical Engineering focus with VIDEO (only here)
    blog_section = ft.Container(
        key="blog",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("TECHNICAL BLOG: ELECTRICAL ENGINEERING INSIGHTS", "Written technical explanations with embedded video demonstrations."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Understanding Ohm's Law in Industrial Systems", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                                    ft.Text("Application of fundamental electrical principles in industrial power distribution and equipment protection systems.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("V = I × R   |   P = I² × R   |   I = V / R", font_family="monospace", size=14, color=PRIMARY_BLUE),
                                    ),
                                    ft.Text("Understanding these relationships is crucial for circuit protection, load calculation, and system design in industrial environments.", color=TEXT_GREY, size=13),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("MineShield Project Demonstration", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                                    ft.Text("Video showcase of the MineShield mine safety monitoring system in action.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        content=ftv.Video(
                                            expand=True,
                                            playlist=[ftv.VideoMedia("/video/video.mp4")],
                                            playlist_mode=ftv.PlaylistMode.LOOP,
                                            fill_color=ACCENT_BLUE,
                                            aspect_ratio=16/9,
                                            volume=100,
                                            autoplay=True,
                                            show_controls=True,
                                            filter_quality=ft.FilterQuality.HIGH,
                                            muted=False,
                                            wakelock=True,
                                        ),
                                        border_radius=8,
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                    ),
                                    ft.Text("Watch the full demonstration of sensor integration, dashboard monitoring, and alert systems.", color=TEXT_GREY, size=12),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 7. Experience / Leadership Section - Electrical Engineering focus
    leadership_section = ft.Container(
        key="experience",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("ELECTRICAL ENGINEERING LEADERSHIP & EXPERIENCE", "Active contributions to engineering community and practical industry exposure."),
                ft.Text("Bridging academic electrical engineering theory with practical industry applications while developing innovative safety solutions.", size=15, color=TEXT_GREY),
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.GROUP, color=PRIMARY_BLUE, size=28),
                                ft.Text("Electrical Engineering Society", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Active member contributing to workshops, industry guest lectures, and technical seminars on emerging electrical technologies.", color=TEXT_GREY, size=13),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.SETTINGS, color=PRIMARY_BLUE, size=28),
                                ft.Text("MineShield Development Team", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Core contributor to MineShield mine safety monitoring system development, testing, and documentation.", color=TEXT_GREY, size=13),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_BLUE, size=28),
                                ft.Text("MathWorks Self-Paced Learning", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Completed comprehensive MATLAB and Simulink certification courses to enhance computational engineering capabilities.", color=TEXT_GREY, size=13),
                            ])
                        ),
                    ]
                )
            ]
        )
    )

    # 8. MATLAB Achievement Hub Section - Updated with your actual files
    certificate_data = [
        {"title": "MATLAB Onramp", "file": "matlab onramp certificate ozil_page-0001.jpg"},
        {"title": "Simulink Onramp", "file": "simulink onramp certificate ozil_page-0001.jpg"},
        {"title": "Core MATLAB Skills", "file": "core matlab skills certificate ozil_page-0001.jpg"},
        {"title": "Calculations with Vectors", "file": "calculations with vertor certificate ozil_page-0001.jpg"},
        {"title": "Machine Learning Onramp", "file": "machine learning onramp certificate ozil additional_page-0001.jpg"},
        {"title": "Simulink Fundamentals", "file": "simulink fundamental certificate ozil_page-0001.jpg"},
        {"title": "The How and Why of Writing Functions", "file": "the how and why of writig functions certificate ozil additional_page-0001.jpg"},
        {"title": "Visualization in MATLAB", "file": "visualization in matlab certificate ozil_page-0001.jpg"},
    ]

    cert_cards = []
    for cert in certificate_data:
        img_control = ft.Image(
            src=f"/images/{cert['file']}",
            height=150,
            fit="contain", 
            scale=1.0,
            animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
        )

        card_design = ft.Container(
            bgcolor=DARK_CARD_BG,
            padding=15,
            border_radius=10,
            border=get_uniform_border(1, ACCENT_BLUE),
            on_click=lambda e, title=cert["title"], file=cert["file"]: open_certificate_zoom(title, file),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=150,
                        width=320,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        border_radius=6,
                        bgcolor=BG_WHITE,
                        alignment=ft.Alignment(0, 0),
                        content=img_control,
                    ),
                    ft.Container(height=6),
                    ft.Text(cert["title"], weight=ft.FontWeight.BOLD, color=DARK_TEXT_WHITE, text_align=ft.TextAlign.CENTER, size=13, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Click to zoom", color=CERT_HINT, size=11, text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

        hover_stack = ft.Stack(
            height=230,
            controls=[
                ft.Container(top=10, left=0, right=0, animate_position=ft.Animation(300, ft.AnimationCurve.EASE_OUT), content=card_design)
            ]
        )

        def make_hover_handler(stack_wrapper, target_img):
            inner_move_container = stack_wrapper.controls[0]
            def handle_hover(e):
                if e.data == "true":
                    inner_move_container.top = 0  
                    inner_move_container.shadow = ft.BoxShadow(blur_radius=12, color=ACCENT_BLUE)
                    target_img.scale = 1.05  
                else:
                    inner_move_container.top = 10  
                    inner_move_container.shadow = None
                    target_img.scale = 1.0
                inner_move_container.update()
                target_img.update()
            return handle_hover

        card_design.on_hover = make_hover_handler(hover_stack, img_control)
        cert_cards.append(ft.Container(col={"sm": 12, "md": 4}, content=hover_stack))

    certification_section = ft.Container(
        key="certificates",
        bgcolor=SECTION_DEEP,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MATLAB & SIMULINK CERTIFICATIONS", "Proof of completion for self-paced courses from MathWorks Learning Center."),
                ft.Text("Click any certificate to zoom in and inspect the completion proof clearly.", size=13, color=SUBTEXT_GREY),
                ft.ResponsiveRow(spacing=20, run_spacing=10, controls=cert_cards),
            ],
        ),
    )

    # 9. GitHub Evidence & Documentation Section
    github_section = ft.Container(
        key="github",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column([
                            ft.Text("GITHUB EVIDENCE & DOCUMENTATION", size=28, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                            ft.Text("Verifiable individual contribution records for MineShield safety project development.", size=15, color=TEXT_GREY),
                        ]),
                        ft.IconButton(icon=ft.Icons.CODE, icon_color=PRIMARY_BLUE, tooltip="GitHub Evidence")
                    ]
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Commit History",
                                "Screenshots showing commits authored by Henock Nahango in the MineShield repository, including dates, messages, and linked files.",
                                ft.Icons.COMMIT,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Pull Request Logs",
                                "Documentation of proposed features, reviews performed, comments resolved, and merges completed during MineShield development.",
                                ft.Icons.MERGE,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Impact Summary",
                                "My code and documentation improved sensor integration, dashboard functionality, and explained engineering outputs for mine safety compliance.",
                                ft.Icons.INSIGHTS,
                            ),
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.FOLDER_SPECIAL, color=PRIMARY_BLUE), ft.Text("MineShield-App", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY)]),
                                    ft.Text("Python/Flet based mine safety monitoring platform with real-time alerts and emergency response features.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Python", size=10, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Flet", size=10, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("MATLAB", size=10, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Active Development", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", style=ft.ButtonStyle(color=ACCENT_BLUE))
                                    ])
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.FOLDER, color=PRIMARY_BLUE), ft.Text("Sensor-Network-ESP32", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY)]),
                                    ft.Text("ESP32-based sensor network for environmental monitoring with gas, temperature, and vibration sensors.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Embedded C", size=10, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("ESP32", size=10, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Stable Release", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", style=ft.ButtonStyle(color=ACCENT_BLUE))
                                    ])
                                ]
                            )
                        ),
                    ],
                ),
            ],
        ),
    )

    # 10. Contact Section Form Setup - Updated with Electrical Engineering info
    name_field = ft.TextField(label="Your Full Name", border_color=PRIMARY_BLUE, focused_border_color=ACCENT_BLUE)
    email_field = ft.TextField(label="Email Address", border_color=PRIMARY_BLUE, focused_border_color=ACCENT_BLUE)
    message_field = ft.TextField(label="Project Details / Inquiry Message", multiline=True, min_lines=4, border_color=PRIMARY_BLUE, focused_border_color=ACCENT_BLUE)

    def handle_submit_message(e):
        if not name_field.value or not email_field.value:
            page.show_snack_bar(ft.SnackBar(content=ft.Text("Please fill out your Name and Email fields before submitting."), bgcolor=ACCENT_BLUE))
        else:
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Thank you {name_field.value}! Your message was compiled and sent successfully."), bgcolor=PRIMARY_BLUE))
            name_field.value = ""
            email_field.value = ""
            message_field.value = ""
            page.update()

    contact_section = ft.Container(
        key="contact",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column([
            create_section_header("GET IN TOUCH", "Collaborate on electrical engineering projects, automation systems, or safety monitoring solutions."),
            ft.ResponsiveRow(
                spacing=30,
                controls=[
                    ft.Column(
                        col={"sm": 12, "md": 5},
                        spacing=15,
                        controls=[
                            ft.Text("Available for Electrical Engineering collaborations, automation projects, power systems research, industrial monitoring solutions, and embedded systems development.", color=TEXT_GREY, size=15),
                            ft.Container(height=10),
                            ft.Row([ft.Icon(ft.Icons.LOCATION_ON, color=PRIMARY_BLUE), ft.Text("Electrical Engineering Campus, University of Namibia, Namibia", color=DEEP_NAVY, weight=ft.FontWeight.W_500)]),
                            ft.Row([ft.Icon(ft.Icons.EMAIL, color=PRIMARY_BLUE), ft.Text("nahangohenock@gmail.com", color=DEEP_NAVY, weight=ft.FontWeight.W_500)]),
                            ft.Row([ft.Icon(ft.Icons.PHONE, color=PRIMARY_BLUE), ft.Text("+264 81 360 9793", color=DEEP_NAVY, weight=ft.FontWeight.W_500)]),
                        ]
                    ),
                    ft.Container(
                        col={"sm": 12, "md": 7},
                        bgcolor=CARD_BG,
                        padding=30,
                        border_radius=12,
                        border=get_uniform_border(1, BORDER_COLOR),
                        content=ft.Column(
                            spacing=15,
                            controls=[
                                ft.Text("Send a Message Directly", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                name_field, email_field, message_field,
                                ft.Container(height=5),
                                ft.ElevatedButton("Submit Message", icon=ft.Icons.SEND, bgcolor=PRIMARY_BLUE, color=BG_WHITE, on_click=handle_submit_message, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6))),
                                ft.Text(
                                    "I consent to having Henock H Nahango store my submitted information so that he can respond to my inquiry.",
                                    size=11,
                                    color=SUBTEXT_GREY,
                                ),
                            ]
                        )
                    )
                ]
            )
        ])
    )

    portfolio_pages = {
        "overview": hero_section,
        "skills": skills_section,
        "contribution": contribution_section,
        "timeline": timeline_section,
        "projects": project_section,
        "blog": blog_section,
        "experience": leadership_section,
        "certificates": certification_section,
        "github": github_section,
        "contact": contact_section,
    }

    page_switcher = ft.AnimatedSwitcher(
        content=build_page_view(hero_section, "overview"),
        duration=220,
        reverse_duration=160,
        switch_in_curve=ft.AnimationCurve.EASE_OUT,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
        transition=ft.AnimatedSwitcherTransition.FADE,
        expand=True,
    )

    def make_nav_button(label, page_key):
        button = ft.TextButton(
            label,
            style=ft.ButtonStyle(
                color=BG_WHITE if page_key == current_page_key["value"] else NAV_INACTIVE,
                overlay_color=OVERLAY_BLUE,
            ),
            on_click=lambda e, target=page_key: navigate_to(target),
        )
        nav_buttons[page_key] = button
        return button

    # =========================================================
    # STICKY NAVBAR PANEL (Pinned permanently to top layer)
    # =========================================================
    header_navbar = ft.Container(
        bgcolor=PRIMARY_BLUE,
        padding=ft.Padding(40, 15, 40, 15),
        border=ft.Border(bottom=ft.BorderSide(1, ACCENT_BLUE)),
        shadow=ft.BoxShadow(blur_radius=10, color=SHADOW_BLUE, offset=ft.Offset(0, 2)),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row([
                    ft.Container(width=12, height=12, bgcolor=BG_WHITE, border_radius=6),
                    ft.Text("HENOCK H NAHANGO", weight=ft.FontWeight.BOLD, size=16, color=BG_WHITE, style=ft.TextStyle(letter_spacing=1.1))
                ], spacing=10),
                ft.Row([
                    make_nav_button("Overview", "overview"),
                    make_nav_button("Skills", "skills"),
                    make_nav_button("Portfolio", "contribution"),
                    make_nav_button("Timeline", "timeline"),
                    make_nav_button("Projects", "projects"),
                    make_nav_button("Blog", "blog"),
                    make_nav_button("Experience", "experience"),
                    make_nav_button("MATLAB Hub", "certificates"),
                    make_nav_button("GitHub", "github"),
                    make_nav_button("Contact", "contact"),
                ], spacing=10, wrap=True)
            ]
        )
    )

    # =========================================================
    # RENDER DIRECT TO MAIN PAGE WINDOW
    # =========================================================
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                header_navbar,
                page_switcher
            ]
        )
    )

if __name__ == "__main__":
    ft.app(
        target=main,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets",
    )
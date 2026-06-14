import os
import flet as ft
import webbrowser
import threading

def main(page: ft.Page):

    # =========================================================
    # PAGE SETTINGS (Optimized for Fixed Header Layout)
    # =========================================================
    page.title = "Henock H Nahango - Electrical Engineering Portfolio | MineShield App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#f0f4f8"
    page.scroll = None

    # =========================================================
    # PROFESSIONAL DARK BLUE COLOR PALETTE
    # =========================================================
    PRIMARY_BLUE = "#1a3a5c"           # Deep Navy Blue
    ACCENT_BLUE = "#2c5f8a"            # Medium Blue
    DEEP_NAVY = "#0d2137"              # Dark Navy for text/buttons
    LIGHT_BG = "#f0f4f8"               # Light blue-tint background
    SECTION_BLUE = "#e8f0f8"           # Very light blue section
    SECTION_DEEP = "#d4e4f0"           # Slightly deeper section
    BG_WHITE = "#ffffff"
    TEXT_GREY = "#2c3e50"              # Dark slate for text
    AVATAR_BG = "#e8f0f8"
    SUBTEXT_GREY = "#5d7a9a"           # Soft blue-grey
    CARD_BG = "#ffffff"
    BORDER_COLOR = "#c5d5e8"           # Soft blue border
    
    DARK_CARD_BG = "#1a3a5c"           # Navy card background
    DARK_TEXT_WHITE = "#ffffff"
    NAV_INACTIVE = "#c5d5e8"           # Light blue for inactive nav
    OVERLAY_BLUE = "#2c5f8a"           # Overlay color
    PROGRESS_TRACK = "#e8f0f8"
    SHADOW_BLUE = "#b0c4de"
    CERT_HINT = "#c5d5e8"

    # Global variable to track active dialog
    active_dialog = None

    def open_certificate_zoom(title: str, image_file: str):
        global active_dialog
        
        # Create dialog content
        zoom_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, color=PRIMARY_BLUE, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=900,
                height=620,
                bgcolor=BG_WHITE,
                padding=10,
                border_radius=8,
                content=ft.Image(src=image_file, fit="contain"),
            ),
            actions=[
                ft.TextButton(
                    "Close", 
                    on_click=lambda e: close_certificate_zoom(),
                    style=ft.ButtonStyle(color=PRIMARY_BLUE)
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        active_dialog = zoom_dialog
        page.dialog = zoom_dialog
        zoom_dialog.open = True
        page.update()

    def close_certificate_zoom():
        global active_dialog
        if active_dialog:
            active_dialog.open = False
            page.update()
            active_dialog = None

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
    
    # 1. Overview Section - WITH LARGER PROFILE PICTURE
    hero_section = ft.Container(
        key="overview",
        bgcolor=LIGHT_BG,
        padding=ft.Padding(50, 60, 50, 60),
        content=ft.ResponsiveRow(
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
                        ft.Text("MineShield App Semester Project Portfolio", size=16, weight=ft.FontWeight.W_500, color=ACCENT_BLUE, italic=True),
                        ft.Divider(color=PRIMARY_BLUE, thickness=1.5),
                        ft.Text("Phone: +264 81 360 9793  |  Email: nahangohenock@gmail.com", size=14, weight=ft.FontWeight.W_500, color=DEEP_NAVY),
                        ft.Text("Electrical Engineering student specializing in power systems, embedded control, signal processing, circuit design, and IoT solutions for mining safety applications. This portfolio is dedicated to my contributions to the MineShield App - a comprehensive mine safety monitoring system.", size=16, color=TEXT_GREY),
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
                            width=280,
                            height=280,
                            border_radius=140,
                            bgcolor=AVATAR_BG,
                            alignment=ft.Alignment(0, 0),
                            border=get_uniform_border(4, PRIMARY_BLUE),
                            content=ft.Image(src="ozil picture.jpg", width=280, height=280, border_radius=140, fit="cover"),
                        ),
                        ft.Container(height=8),
                        ft.Text("Electrical Engineering & Mine Safety Systems 2026", size=12, color=SUBTEXT_GREY, italic=True),
                    ],
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
            create_section_header("CORE ELECTRICAL & TECHNICAL MATRIX", "Integrated expertise across power systems, control theory, and IoT solutions."),
            ft.ResponsiveRow([
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Power & Energy Systems", weight=ft.FontWeight.BOLD, color=ACCENT_BLUE, size=16),
                    create_skill_chip("Power System Analysis", 0.88),
                    create_skill_chip("Renewable Energy Integration", 0.85),
                    create_skill_chip("Electrical Machine Design", 0.82),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Control & Embedded Systems", weight=ft.FontWeight.BOLD, color=ACCENT_BLUE, size=16),
                    create_skill_chip("MATLAB/Simulink", 0.85),
                    create_skill_chip("Microcontroller Programming", 0.80),
                    create_skill_chip("PLC & SCADA Systems", 0.75),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("IoT & Data Analytics", weight=ft.FontWeight.BOLD, color=ACCENT_BLUE, size=16),
                    create_skill_chip("Python for Engineering", 0.82),
                    create_skill_chip("Sensor Networks", 0.78),
                    create_skill_chip("Data Visualization", 0.80),
                ]),
            ], spacing=20)
        ])
    )

    # 3. Individual Portfolio Reflection Section - MineShield App Focus
    contribution_section = ft.Container(
        key="contribution",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MINESHIELD APP - INDIVIDUAL CONTRIBUTION", "Reflection, evidence, lessons learned, challenges, and showcase material."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "MineShield Project Contribution",
                                "I contributed to visitor mode requirements gathering, visitor dashboard testing, read-only verification, and emergency contact validation for the MineShield App.",
                                ft.Icons.SHIELD,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Evidence of Work",
                                "This portfolio includes MATLAB certificate screenshots, visitor demo scripts, APK installation logs, and technical explanations verified during assessment.",
                                ft.Icons.FACT_CHECK,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "What I Learned",
                                "I strengthened my ability to test user-facing features, validate emergency protocols, and document visitor-mode requirements for safety-critical applications.",
                                ft.Icons.LIGHTBULB,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Challenges Addressed",
                                "The main challenge was ensuring read-only verification and visitor dashboard testing. I addressed it by systematic testing, GitHub evidence, and demo scripts.",
                                ft.Icons.TROUBLESHOOT,
                            ),
                        ),
                    ],
                ),
                ft.Container(
                    bgcolor=LIGHT_BG,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column([
                                ft.Text("Individual Contribution Video", size=18, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("3-minute visitor demo (View zones/alerts only) plus Q&A for FR-014", color=TEXT_GREY, size=13),
                            ]),
                            ft.TextButton("Video Link Placeholder", icon=ft.Icons.VIDEO_LIBRARY, url="https://example.com/mineshield-demo", style=ft.ButtonStyle(color=ACCENT_BLUE)),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 4. Project Timeline Section
    timeline_section = ft.Container(
        key="timeline",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MINESHIELD PROJECT TIMELINE", "Weekly log of my specific contributions to the semester group project."),
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Text("Week 1-2: Role Assignment & Project Charter", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Assigned as Electrical Systems Lead for MineShield App. Participated in initial meetings, defined visitor mode requirements, and contributed to project charter documentation.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 3-4: Visitor Mode Requirements Gathering", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Gathered and documented visitor mode specifications for the MineShield App, focusing on guest access, view-only permissions, and safety alert visibility.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 5-6: Visitor Dashboard Testing & Read-Only Verification", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Conducted comprehensive testing of the visitor dashboard, verified read-only functionality, and ensured proper access restrictions for guest users.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 7-8: Visitor Demo Script & Emergency Contact Validation", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Created visitor demonstration script for stakeholder presentations and validated emergency contact features for visitor access mode.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 9-10: APK Installation on Phone #3 (Android 11) & Rehearsal", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Successfully installed and tested APK on Android 11 device (Phone #3), performed rehearsal runs for final demonstration.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Final Week: 3-Minute Visitor Demo (View zones/alerts only) & Q&A for FR-014", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                            ft.Text("Delivered 3-minute visitor demonstration focusing on view zones and alerts, participated in Q&A session for functional requirement FR-014, and completed final submission.", color=TEXT_GREY),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 5. Projects Section - MineShield Electrical Focus
    project_section = ft.Container(
        key="projects",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MINESHIELD APP - ELECTRICAL ENGINEERING PROJECTS", "Core electrical systems designed for mine safety monitoring."),
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
                                    ft.Text("1. MineShield Sensor Network Design", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                                    ft.Text("Multi-sensor array for real-time monitoring of hazardous gas levels, temperature, humidity, and seismic activity in underground mining environments.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("SENSOR NETWORK SPECIFICATIONS:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                            ft.Text("• Gas Sensor: MQ-7 (CO detection range 20-2000 ppm)", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• Temperature/Humidity: DHT22 (±0.5°C accuracy)", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• Seismic Sensor: ADXL345 (3-axis accelerometer)", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• Sampling Rate: 100 Hz per sensor channel", size=12, font_family="monospace", color=ACCENT_BLUE),
                                        ])
                                    ),
                                    ft.Text("Enables real-time hazard detection with IoT connectivity, data logging, and immediate alert system for mine worker safety.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("Arduino/ESP32", size=11, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Sensor Fusion", size=11, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=5, border_radius=4),
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
                                    ft.Text("2. Visitor Mode Access Control System", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                                    ft.Text("Secure read-only access system for visitors with view zones and alerts functionality, implementing FR-014 requirements for mine safety monitoring.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("ACCESS CONTROL FEATURES:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                            ft.Text("• Read-only dashboard for visitor accounts", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• View zones: Live hazard monitoring display", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• Alert visibility without modification rights", size=12, font_family="monospace", color=ACCENT_BLUE),
                                            ft.Text("• Emergency contact display for visitors", size=12, font_family="monospace", color=ACCENT_BLUE),
                                        ])
                                    ),
                                    ft.Text("Ensures safe guest access to mine safety data while maintaining system integrity and data protection protocols.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("Android APK", size=11, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Read-Only Mode", size=11, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 6. Technical Blog Section
    blog_section = ft.Container(
        key="blog",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("TECHNICAL BLOG: ELECTRICAL ENGINEERING CONCEPTS", "Written technical explanations with embedded video insert placeholders."),
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
                                    ft.Text("Ohm's Law & Power Calculations", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                                    ft.Text("For electrical engineering modules, voltage, current, and resistance relationships are fundamental. Correct notation ensures accurate circuit analysis.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("V = I × R   |   P = V × I = I² × R = V²/R", font_family="monospace", size=14, color=PRIMARY_BLUE),
                                    ),
                                    ft.Text("Where V is voltage (volts), I is current (amperes), R is resistance (ohms), and P is power (watts).", color=TEXT_GREY, size=13),
                                    ft.TextButton("Embedded Video Insert", icon=ft.Icons.PLAY_CIRCLE, url="https://example.com/ohms-law-video", style=ft.ButtonStyle(color=ACCENT_BLUE)),
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
                                    ft.Text("Signal Processing for Sensors", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_BLUE),
                                    ft.Text("In the MineShield project, structured filtering and signal conditioning helped convert raw sensor data into actionable safety alerts.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("V_out = V_in × (R2/(R1+R2)) | f_c = 1/(2πRC)", font_family="monospace", size=14, color=PRIMARY_BLUE),
                                    ),
                                    ft.Text("Voltage dividers and low-pass filters ensure accurate sensor readings by removing high-frequency noise.", color=TEXT_GREY, size=13),
                                    ft.TextButton("Embedded Video Insert", icon=ft.Icons.PLAY_CIRCLE, url="https://example.com/signal-processing-video", style=ft.ButtonStyle(color=ACCENT_BLUE)),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 7. Experience / Leadership Section
    leadership_section = ft.Container(
        key="experience",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("ELECTRICAL ENGINEERING LEADERSHIP & FIELD EXPERIENCE", "Active contributions to the electrical engineering community and practical industry exposure."),
                ft.Text("Bridging academic electrical theory with practical industry applications while mentoring aspiring electrical engineers.", size=15, color=TEXT_GREY),
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.WORKSPACE_PREMIUM, color=PRIMARY_BLUE, size=28),
                                ft.Text("Mine Safety Systems Intern", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Assisted in installing and testing environmental monitoring sensors at a local mine. Gained practical experience with data logging from gas and vibration sensors.", color=TEXT_GREY, size=13),
                                ft.Text("• Calibrated CO and methane sensors", size=12, color=TEXT_GREY),
                                ft.Text("• Analyzed sensor data logs for anomalies", size=12, color=TEXT_GREY),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCIENCE, color=PRIMARY_BLUE, size=28),
                                ft.Text("Electrical Workshop Facilitator", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Led a 3-day workshop on Arduino-based data acquisition for 20+ high school students, introducing them to basic circuit design and sensor integration.", color=TEXT_GREY, size=13),
                                ft.Text("• Designed a simple temperature logger", size=12, color=TEXT_GREY),
                                ft.Text("• Supervised student-led mini-projects", size=12, color=TEXT_GREY),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.DOCUMENT_SCANNER, color=PRIMARY_BLUE, size=28),
                                ft.Text("Technical Documentation Volunteer", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Contributed to writing user manuals for a solar-powered water pumping system, helping local technicians with maintenance and troubleshooting.", color=TEXT_GREY, size=13),
                                ft.Text("• Created easy-to-follow wiring diagrams", size=12, color=TEXT_GREY),
                                ft.Text("• Translated technical terms into practical steps", size=12, color=TEXT_GREY),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.CODE, color=PRIMARY_BLUE, size=28),
                                ft.Text("MATLAB Student Ambassador", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                ft.Text("Promoted the use of MATLAB and Simulink within my department by organizing study sessions and solving problems collaboratively with peers.", color=TEXT_GREY, size=13),
                                ft.Text("• Assisted 15+ students with lab work", size=12, color=TEXT_GREY),
                                ft.Text("• Shared tips for efficient data plotting", size=12, color=TEXT_GREY),
                            ])
                        ),
                    ]
                )
            ]
        )
    )

    # 8. MATLAB Achievement Hub Section - Using your actual image files
    certificate_data = [
        {"title": "Calculations with Vectors", "file": "calculations with vertor certificate ozil_page-0001.jpg"},
        {"title": "Core MATLAB Skills", "file": "core matlab skills certificate ozil_page-0001.jpg"},
        {"title": "Machine Learning Onramp", "file": "machine learning onramp certificate ozil additional_page-0001.jpg"},
        {"title": "MATLAB Onramp", "file": "matlab onramp certificate ozil_page-0001.jpg"},
        {"title": "Simulink Fundamentals", "file": "simulink fundamental certificate ozil_page-0001.jpg"},
        {"title": "Simulink Onramp", "file": "simulink onramp certificate ozil_page-0001.jpg"},
        {"title": "The How and Why of Writing Functions", "file": "the how and why of writig functions certificate ozil additional_page-0001.jpg"},
        {"title": "Visualization in MATLAB", "file": "visualization in matlab certificate ozil_page-0001.jpg"},
    ]

    cert_cards = []
    for cert in certificate_data:
        img_control = ft.Image(
            src=cert['file'],
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
                create_section_header("MATLAB ACHIEVEMENT HUB", "Proof of completion for MATLAB and Simulink courses from the MathWorks Learning Center."),
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
                            ft.Text("Verifiable individual contribution records for the MineShield App semester project team.", size=15, color=TEXT_GREY),
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
                                "Screenshots showing commits authored by Henock H Nahango for visitor mode features, dashboard testing, and read-only verification.",
                                ft.Icons.COMMIT,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Pull Request Logs",
                                "Document proposed features for visitor dashboard, reviews performed, comments resolved, and merges completed for FR-014 implementation.",
                                ft.Icons.MERGE,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Impact Summary",
                                "My code and documentation improved visitor access control, emergency contact validation, and APK deployment testing on Android 11 devices.",
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
                                    ft.Row([ft.Icon(ft.Icons.SENSORS, color=PRIMARY_BLUE), ft.Text("MineShield-Visitor-Mode", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY)]),
                                    ft.Text("Visitor dashboard with read-only access, view zones for hazard monitoring, and emergency contact display for guest users.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Android", size=10, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Read-Only", size=10, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("FR-014", size=10, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Android 11 Tested", size=11, color=SUBTEXT_GREY),
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
                                    ft.Row([ft.Icon(ft.Icons.EMERGENCY, color=PRIMARY_BLUE), ft.Text("Emergency-Contact-Validation", size=16, weight=ft.FontWeight.BOLD, color=DEEP_NAVY)]),
                                    ft.Text("Emergency contact verification system for visitor mode with validation protocols and alert testing procedures.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Validation", size=10, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Testing", size=10, color=DEEP_NAVY), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Demo Ready", size=11, color=SUBTEXT_GREY),
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

    # 10. Advanced Contact Section
    name_field = ft.TextField(
        label="Your Full Name",
        border_color=PRIMARY_BLUE,
        focused_border_color=ACCENT_BLUE,
        text_style=ft.TextStyle(color=DEEP_NAVY)
    )
    email_field = ft.TextField(
        label="Email Address",
        border_color=PRIMARY_BLUE,
        focused_border_color=ACCENT_BLUE,
        text_style=ft.TextStyle(color=DEEP_NAVY)
    )
    subject_field = ft.Dropdown(
        label="Subject (Reason for Contact)",
        border_color=PRIMARY_BLUE,
        focused_border_color=ACCENT_BLUE,
        options=[
            ft.dropdown.Option("Project Collaboration"),
            ft.dropdown.Option("MineShield App Inquiry"),
            ft.dropdown.Option("Research Opportunity"),
            ft.dropdown.Option("Internship/Job Opportunity"),
            ft.dropdown.Option("Technical Question"),
            ft.dropdown.Option("Other"),
        ],
        text_style=ft.TextStyle(color=DEEP_NAVY)
    )
    message_field = ft.TextField(
        label="Detailed Message",
        multiline=True,
        min_lines=5,
        max_lines=8,
        border_color=PRIMARY_BLUE,
        focused_border_color=ACCENT_BLUE,
        text_style=ft.TextStyle(color=DEEP_NAVY)
    )
    consent_checkbox = ft.Checkbox(
        label="I consent to having Henock H Nahango store my submitted information for the purpose of responding to my inquiry.",
        fill_color=PRIMARY_BLUE,
        check_color=BG_WHITE,
        value=False
    )

    def handle_submit_message(e):
        # Validation
        if not name_field.value or not email_field.value or not message_field.value or not subject_field.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please fill out all required fields (Name, Email, Subject, and Message)."),
                    bgcolor=ACCENT_BLUE,
                    action="Close",
                    action_color=BG_WHITE
                )
            )
        elif "@" not in email_field.value or "." not in email_field.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please enter a valid email address."),
                    bgcolor=ACCENT_BLUE,
                    action="Close",
                    action_color=BG_WHITE
                )
            )
        elif not consent_checkbox.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please consent to the data storage policy before submitting."),
                    bgcolor=ACCENT_BLUE,
                    action="Close",
                    action_color=BG_WHITE
                )
            )
        else:
            # Simulate sending message
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text(f"Thank you {name_field.value}! Your message regarding '{subject_field.value}' has been received. I'll respond to {email_field.value} soon."),
                    bgcolor=PRIMARY_BLUE,
                    action="Dismiss",
                    action_color=BG_WHITE,
                    duration=5000
                )
            )
            # Clear form after submission
            name_field.value = ""
            email_field.value = ""
            subject_field.value = None
            message_field.value = ""
            consent_checkbox.value = False
            page.update()

    def clear_form():
        name_field.value = ""
        email_field.value = ""
        subject_field.value = None
        message_field.value = ""
        consent_checkbox.value = False
        page.update()
        page.show_snack_bar(
            ft.SnackBar(
                content=ft.Text("Form cleared successfully."),
                bgcolor=PRIMARY_BLUE,
                action="Close",
                action_color=BG_WHITE
            )
        )

    contact_section = ft.Container(
        key="contact",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column([
            create_section_header("GET IN TOUCH", "Collaborate on electrical engineering projects, MineShield App development, or research opportunities."),
            ft.ResponsiveRow(
                spacing=30,
                controls=[
                    ft.Column(
                        col={"sm": 12, "md": 5},
                        spacing=20,
                        controls=[
                            ft.Text("Available for electrical engineering consultation, IoT sensor network design, power systems analysis, and research collaborations on mine safety technology.", color=TEXT_GREY, size=15),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("📍 Namibia (Electrical Engineering Campus)", color=DEEP_NAVY, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("✉️ nahangohenock@gmail.com", color=DEEP_NAVY, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("📱 +264 81 360 9793", color=DEEP_NAVY, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("⏱ Response time: 24-48 hours", color=TEXT_GREY, size=13),
                            ft.Card(
                                elevation=2,
                                content=ft.Container(
                                    bgcolor=SECTION_BLUE,
                                    padding=15,
                                    border_radius=8,
                                    content=ft.Column([
                                        ft.Text("Preferred Contact Methods:", weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                        ft.Text("• Email for project proposals", size=13, color=TEXT_GREY),
                                        ft.Text("• LinkedIn for professional networking", size=13, color=TEXT_GREY),
                                        ft.Text("• Phone for urgent mine safety matters", size=13, color=TEXT_GREY),
                                    ])
                                )
                            )
                        ]
                    ),
                    ft.Container(
                        col={"sm": 12, "md": 7},
                        bgcolor=CARD_BG,
                        padding=30,
                        border_radius=12,
                        border=get_uniform_border(1, BORDER_COLOR),
                        content=ft.Column(
                            spacing=20,
                            controls=[
                                ft.Text("Send a Message About MineShield App or Collaboration", size=18, weight=ft.FontWeight.BOLD, color=DEEP_NAVY),
                                name_field,
                                email_field,
                                subject_field,
                                message_field,
                                consent_checkbox,
                                ft.Divider(color=BORDER_COLOR),
                                ft.Row([
                                    ft.ElevatedButton(
                                        "Submit Message",
                                        icon=ft.Icons.SEND,
                                        bgcolor=PRIMARY_BLUE,
                                        color=BG_WHITE,
                                        on_click=handle_submit_message,
                                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6))
                                    ),
                                    ft.TextButton(
                                        "Clear Form",
                                        on_click=lambda e: clear_form(),
                                        style=ft.ButtonStyle(color=ACCENT_BLUE)
                                    )
                                ], alignment=ft.MainAxisAlignment.END)
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
    # STICKY NAVBAR PANEL
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

# =========================================================
# UPDATED RENDER DEPLOYMENT CONFIGURATION - FIXES "NOT FOUND" ERROR
# =========================================================
if __name__ == "__main__":
    # Get the port from environment variable (Render sets this automatically)
    port = int(os.environ.get("PORT", 8080))
    
    # Print debug info to Render logs
    print(f"Starting Flet application on port {port}")
    print(f"Assets directory: {os.path.join(os.path.dirname(__file__), 'assets')}")
    
    # CRUCIAL: host="0.0.0.0" allows Render to route external traffic to your app
    # view=ft.AppView.WEB_BROWSER ensures web rendering mode
    ft.app(
        target=main, 
        host="0.0.0.0",  # ← MUST be 0.0.0.0 for Render
        port=port, 
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets"
    )
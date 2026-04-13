import warnings
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.patches as mpatches
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
warnings.filterwarnings('ignore')

# ============================================
# 1) إنشاء البيانات
# ============================================
data = {
    'Order_ID': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
                 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
                 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029,
                 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039,
                 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049,
                 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059,
                 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069,
                 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079,
                 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089,
                 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099,
                 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109,
                 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119,
                 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129,
                 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139,
                 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149],
    'Date': ['2024-05-16', '2024-01-30', '2024-01-06', '2024-06-09', '2024-02-08',
             '2024-06-18', '2024-02-23', '2024-07-15', '2024-01-27', '2024-03-07',
             '2024-07-19', '2024-07-12', '2024-04-14', '2024-05-09', '2024-03-18',
             '2024-03-04', '2024-01-17', '2024-01-14', '2024-02-19', '2024-03-27',
             '2024-01-11', '2024-02-02', '2024-01-09', '2024-02-18', '2024-05-03',
             '2024-01-12', '2024-04-11', '2024-04-29', '2024-01-26', '2024-01-15',
             '2024-04-12', '2024-05-06', '2024-04-23', '2024-01-06', '2024-07-17',
             '2024-03-27', '2024-04-10', '2024-01-07', '2024-01-17', '2024-07-02',
             '2024-06-16', '2024-07-18', '2024-06-24', '2024-01-13', '2024-04-22',
             '2024-05-24', '2024-01-28', '2024-01-14', '2024-03-12', '2024-01-30',
             '2024-03-11', '2024-04-14', '2024-06-12', '2024-04-08', '2024-04-19',
             '2024-01-24', '2024-06-12', '2024-07-10', '2024-01-07', '2024-01-29',
             '2024-05-23', '2024-06-24', '2024-04-21', '2024-05-17', '2024-07-15',
             '2024-01-15', '2024-01-30', '2024-03-15', '2024-07-09', '2024-06-29',
             '2024-02-16', '2024-02-25', '2024-01-01', '2024-05-24', '2024-04-11',
             '2024-04-06', '2024-06-18', '2024-02-25', '2024-05-26', '2024-05-17',
             '2024-02-05', '2024-04-17', '2024-06-08', '2024-03-02', '2024-04-20',
             '2024-04-02', '2024-01-10', '2024-03-02', '2024-04-29', '2024-03-31',
             '2024-07-11', '2024-01-06', '2024-03-19', '2024-03-06', '2024-01-20',
             '2024-05-20', '2024-03-07', '2024-03-10', '2024-05-21', '2024-02-12',
             '2024-01-15', '2024-02-16', '2024-02-02', '2024-04-20', '2024-05-05',
             '2024-04-18', '2024-06-28', '2024-03-06', '2024-02-04', '2024-01-22',
             '2024-01-10', '2024-07-10', '2024-04-27', '2024-05-05', '2024-04-29',
             '2024-04-23', '2024-06-06', '2024-07-09', '2024-02-26', '2024-05-25',
             '2024-01-02', '2024-06-07', '2024-01-17', '2024-05-04', '2024-04-28',
             '2024-01-24', '2024-03-02', '2024-07-19', '2024-06-27', '2024-05-25',
             '2024-02-07', '2024-04-01', '2024-02-14', '2024-05-03', '2024-04-19',
             '2024-01-01', '2024-01-27', '2024-06-08', '2024-05-25', '2024-01-25',
             '2024-05-31', '2024-06-04', '2024-05-26', '2024-01-13', '2024-03-15',
             '2024-06-19', '2024-04-18', '2024-05-03', '2024-03-02', '2024-07-01'],
    'Product': ['Desk', 'Desk', 'Sofa', 'Desk', 'Desk', 'Table', 'Chair', 'Lamp', 'Lamp', 'Lamp',
                'Lamp', 'Chair', 'Table', 'Sofa', 'Desk', 'Sofa', 'Desk', 'Chair', 'Table', 'Chair',
                'Table', 'Lamp', 'Desk', 'Sofa', 'Chair', 'Lamp', 'Lamp', 'Desk', 'Desk', 'Desk',
                'Table', 'Desk', 'Table', 'Lamp', 'Chair', 'Desk', 'Table', 'Table', 'Table', 'Lamp',
                'Desk', 'Sofa', 'Chair', 'Sofa', 'Chair', 'Sofa', 'Chair', 'Sofa', 'Sofa', 'Sofa',
                'Chair', 'Table', 'Lamp', 'Chair', 'Lamp', 'Table', 'Chair', 'Table', 'Lamp', 'Table',
                'Desk', 'Table', 'Desk', 'Desk', 'Table', 'Desk', 'Desk', 'Sofa', 'Sofa', 'Table',
                'Desk', 'Lamp', 'Sofa', 'Chair', 'Desk', 'Table', 'Chair', 'Table', 'Lamp', 'Chair',
                'Table', 'Sofa', 'Table', 'Chair', 'Table', 'Table', 'Desk', 'Table', 'Table', 'Chair',
                'Lamp', 'Table', 'Chair', 'Sofa', 'Table', 'Table', 'Desk', 'Chair', 'Desk', 'Desk',
                'Sofa', 'Desk', 'Table', 'Lamp', 'Chair', 'Chair', 'Chair', 'Desk', 'Desk', 'Chair',
                'Sofa', 'Desk', 'Sofa', 'Chair', 'Chair', 'Sofa', 'Chair', 'Chair', 'Table', 'Chair',
                'Lamp', 'Lamp', 'Table', 'Table', 'Table', 'Lamp', 'Table', 'Chair', 'Desk', 'Table',
                'Table', 'Sofa', 'Table', 'Chair', 'Table', 'Table', 'Sofa', 'Desk', 'Chair', 'Desk',
                'Sofa', 'Chair', 'Desk', 'Table', 'Table', 'Sofa', 'Chair', 'Desk', 'Chair', 'Desk'],
    'Region': ['West', 'North', 'West', 'East', 'North', 'North', 'North', 'West', 'North', 'South',
               'West', 'North', 'West', 'West', 'South', 'North', 'West', 'South', 'North', 'South',
               'South', 'West', 'North', 'North', 'West', 'North', 'East', 'North', 'East', 'East',
               'East', 'West', 'East', 'West', 'East', 'West', 'West', 'East', 'South', 'East',
               'South', 'North', 'South', 'East', 'East', 'North', 'East', 'West', 'West', 'East',
               'East', 'East', 'East', 'West', 'West', 'North', 'East', 'North', 'East', 'North',
               'East', 'East', 'South', 'West', 'South', 'West', 'East', 'North', 'North', 'East',
               'West', 'East', 'East', 'South', 'West', 'East', 'North', 'South', 'East', 'East',
               'North', 'West', 'West', 'West', 'North', 'West', 'West', 'East', 'East', 'East',
               'North', 'North', 'East', 'East', 'East', 'South', 'West', 'East', 'South', 'West',
               'North', 'West', 'East', 'East', 'South', 'South', 'North', 'East', 'South', 'North',
               'East', 'East', 'East', 'East', 'South', 'East', 'North', 'West', 'North', 'East',
               'East', 'South', 'South', 'North', 'South', 'South', 'East', 'South', 'North', 'South',
               'West', 'East', 'North', 'North', 'North', 'South', 'North', 'West', 'North', 'South',
               'West', 'North', 'West', 'West', 'East', 'North', 'North', 'East', 'West', 'South'],
    'Quantity': [6, 7, 5, 10, 3, 6, 2, 8, 5, 4, 6, 3, 6, 4, 10, 6, 7, 7, 3, 8,
                 3, 4, 9, 10, 4, 1, 4, 2, 10, 5, 9, 8, 8, 3, 9, 5, 6, 9, 8, 10,
                 9, 10, 3, 1, 8, 7, 8, 8, 7, 4, 3, 5, 2, 1, 4, 2, 8, 7, 9, 10,
                 8, 7, 7, 3, 2, 8, 1, 7, 1, 10, 8, 8, 3, 8, 2, 5, 9, 1, 3, 8,
                 2, 8, 6, 8, 1, 2, 1, 3, 6, 6, 7, 6, 10, 2, 2, 5, 7, 5, 3, 2,
                 3, 6, 9, 3, 7, 4, 4, 5, 3, 9, 5, 3, 4, 2, 8, 1, 7, 2, 6, 7,
                 8, 9, 10, 1, 10, 6, 8, 7, 9, 10, 4, 6, 6, 9, 4, 4, 9, 6, 1, 4,
                 2, 8, 5, 4, 7, 5, 10, 8, 5, 8],
    'Revenue': [2460, 931, 760, 740, 672, 2040, 558, 2712, 915, 1160,
                1896, 423, 1770, 1920, 4120, 2562, 714, 861, 1080, 2640,
                378, 720, 3978, 4440, 1044, 418, 1376, 414, 4070, 2190,
                3843, 3144, 2032, 252, 2169, 290, 858, 1656, 680, 4550,
                2394, 2730, 1032, 494, 3360, 1372, 400, 1216, 2261, 880,
                357, 915, 692, 475, 1236, 430, 1744, 2156, 2628, 3130,
                2568, 3024, 1757, 153, 556, 3592, 272, 630, 385, 4300,
                3816, 3264, 492, 2392, 306, 1795, 1305, 316, 843, 1896,
                846, 2472, 2190, 2736, 286, 630, 222, 1221, 1404, 2160,
                588, 2670, 1730, 502, 912, 700, 3360, 1645, 1455, 238,
                627, 816, 3825, 771, 3451, 1112, 1300, 595, 867, 2088,
                2425, 195, 1452, 986, 3528, 419, 2863, 730, 2070, 1323,
                2624, 1773, 2490, 73, 1130, 2796, 2280, 910, 2988, 1830,
                284, 1644, 2580, 3906, 1336, 324, 3267, 1812, 493, 960,
                278, 1104, 505, 772, 1967, 2455, 3880, 3464, 1475, 2496],
    'Profit': [1079.7, 260.68, 184.39, 151.6, 153.99, 731.92, 176.44, 1344.29, 444.61, 355.2,
               867.77, 91.18, 676.84, 772.35, 880.02, 1214.14, 264.81, 195.76, 331.74, 1130.98,
               118.3, 341.92, 1442.41, 1174.03, 316.5, 153.33, 611.58, 133.95, 967.6, 1081.28,
               1785.26, 683.95, 1013.89, 93.81, 902.65, 144.05, 407.16, 777.18, 325.57, 1889.82,
               1138.83, 552.33, 230.62, 134.41, 1028.44, 355.67, 171.76, 427.72, 762.89, 383.39,
               130.61, 184.83, 270.72, 123.09, 297.54, 94.14, 567.73, 1073, 894.68, 1384.75,
               588.28, 927.31, 800.87, 48.74, 270.08, 917.33, 59.73, 264.53, 131.64, 1195,
               1006.65, 769.11, 187.32, 545.64, 97.43, 760.6, 443.25, 81.39, 268.79, 494.64,
               295.72, 621.84, 474.28, 989.34, 96.32, 182.36, 45.34, 258.77, 303.68, 882.58,
               223.06, 1165.75, 810.88, 193.68, 403.33, 224.21, 1493.5, 367.98, 593.16, 114.28,
               165.38, 289.93, 947.05, 354.3, 834.46, 410.37, 507.83, 130.64, 433.22, 588.07,
               509.96, 85.58, 596.25, 234.78, 874.97, 149.09, 815.33, 355.43, 578.9, 537.5,
               902.04, 476.19, 747.55, 29.65, 366.22, 1012.84, 595.27, 425.04, 1113.51, 618.69,
               107.41, 477.34, 874.49, 1642.78, 311.3, 136.15, 849.11, 705.43, 121.68, 330.04,
               125.99, 358.05, 179.24, 375.97, 753.38, 908.49, 1300.95, 1115.45, 719.45, 882.23]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# ============================================
# 2) تنظيف البيانات
# ============================================
df = df.drop_duplicates()
df = df.dropna()
df = df[df['Quantity'] > 0]
df = df[df['Revenue'] > 0]

# ============================================
# 3) حساب المؤشرات
# ============================================
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()
total_orders = len(df)
avg_order_value = total_revenue / total_orders
profit_margin = (total_profit / total_revenue) * 100
avg_quantity = df['Quantity'].mean()

# تحليلات
product_summary = df.groupby('Product').agg(
    Revenue=('Revenue', 'sum'), Profit=('Profit', 'sum'), Orders=('Order_ID', 'count')
).reset_index()

region_summary = df.groupby('Region').agg(
    Revenue=('Revenue', 'sum'), Profit=('Profit', 'sum'), Orders=('Order_ID', 'count')
).reset_index()

df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%b')
monthly_summary = df.groupby(['Month', 'Month_Name']).agg(
    Revenue=('Revenue', 'sum'), Profit=('Profit', 'sum'), Orders=('Order_ID', 'count')
).reset_index().sort_values('Month')

# أفضل وأسوأ منتج
best_product = product_summary.loc[product_summary['Revenue'].idxmax(
), 'Product']
worst_product = product_summary.loc[product_summary['Revenue'].idxmin(
), 'Product']
best_region = region_summary.loc[region_summary['Revenue'].idxmax(), 'Region']

# ============================================
# ألوان
# ============================================
DARK_BLUE = '#1B2A4A'
MEDIUM_BLUE = '#2E86AB'
LIGHT_BLUE = '#D6EAF8'
GREEN = '#27AE60'
GOLD = '#F39C12'
RED = '#E74C3C'
GRAY = '#95A5A6'
BG_COLOR = '#FAFBFC'
CARD_BG = '#FFFFFF'
colors_palette = ['#2E86AB', '#A23B72',
                  '#F18F01', '#C73E1D', '#3B1F2B', '#27AE60']

# ============================================
# 4) إنشاء PDF
# ============================================
pdf_file = "Sales_Dashboard_Report.pdf"

with PdfPages(pdf_file) as pdf:

    # ==========================================
    # الصفحة 1: صفحة الغلاف
    # ==========================================
    fig_cover = plt.figure(figsize=(11.69, 8.27))  # A4 Landscape
    fig_cover.patch.set_facecolor(DARK_BLUE)

    # إطار خارجي
    border = mpatches.FancyBboxPatch(
        (0.03, 0.03), 0.94, 0.94,
        boxstyle="round,pad=0.02",
        facecolor='none', edgecolor='#FFFFFF', linewidth=2,
        transform=fig_cover.transFigure
    )
    fig_cover.patches.append(border)

    # خط زخرفي علوي
    fig_cover.patches.append(mpatches.FancyBboxPatch(
        (0.15, 0.72), 0.70, 0.008,
        boxstyle="round,pad=0.003",
        facecolor=GOLD, edgecolor='none',
        transform=fig_cover.transFigure
    ))

    # خط زخرفي سفلي
    fig_cover.patches.append(mpatches.FancyBboxPatch(
        (0.15, 0.38), 0.70, 0.008,
        boxstyle="round,pad=0.003",
        facecolor=GOLD, edgecolor='none',
        transform=fig_cover.transFigure
    ))

    # العنوان الرئيسي
    fig_cover.text(0.5, 0.62, 'SALES DASHBOARD', fontsize=42,
                   fontweight='bold', color='#FFFFFF',
                   ha='center', va='center', fontfamily='sans-serif')

    fig_cover.text(0.5, 0.53, 'REPORT', fontsize=36,
                   fontweight='light', color=GOLD,
                   ha='center', va='center', fontfamily='sans-serif',
                   style='italic')

    # معلومات
    fig_cover.text(0.5, 0.43, 'January 2024 — July 2024', fontsize=16,
                   color='#BDC3C7', ha='center', va='center',
                   fontfamily='sans-serif')

    # أيقونة
    fig_cover.text(0.5, 0.82, '📊', fontsize=50,
                   ha='center', va='center')

    # معلومات أسفل
    fig_cover.text(0.5, 0.22, f'Total Revenue: ${total_revenue:,.0f}  |  '
                   f'Total Profit: ${total_profit:,.0f}  |  '
                   f'Orders: {total_orders}',
                   fontsize=13, color='#BDC3C7', ha='center', va='center',
                   fontfamily='sans-serif')

    fig_cover.text(0.5, 0.12, 'Generated by Python Analytics Engine',
                   fontsize=10, color='#7F8C8D', ha='center', va='center',
                   fontfamily='sans-serif', style='italic')

    plt.axis('off')
    pdf.savefig(fig_cover, facecolor=fig_cover.get_facecolor())
    plt.close(fig_cover)

    # ==========================================
    # الصفحة 2: KPIs + ملخص
    # ==========================================
    fig_kpi = plt.figure(figsize=(11.69, 8.27))
    fig_kpi.patch.set_facecolor(BG_COLOR)

    # شريط العنوان العلوي
    fig_kpi.patches.append(mpatches.FancyBboxPatch(
        (0.02, 0.91), 0.96, 0.07,
        boxstyle="round,pad=0.01",
        facecolor=DARK_BLUE, edgecolor='none',
        transform=fig_kpi.transFigure
    ))
    fig_kpi.text(0.5, 0.945, 'KEY PERFORMANCE INDICATORS',
                 fontsize=20, fontweight='bold', color='#FFFFFF',
                 ha='center', va='center', fontfamily='sans-serif')

    # --- KPI Cards ---
    kpi_info = [
        ('TOTAL REVENUE', f'${total_revenue:,.0f}', MEDIUM_BLUE, '💰'),
        ('TOTAL PROFIT', f'${total_profit:,.0f}', GREEN, '📈'),
        ('TOTAL ORDERS', f'{total_orders}', GOLD, '📦'),
        ('AVG ORDER VALUE', f'${avg_order_value:,.0f}', '#8E44AD', '🛒'),
        ('PROFIT MARGIN', f'{profit_margin:.1f}%', RED, '📊'),
        ('AVG QUANTITY', f'{avg_quantity:.1f}', '#16A085', '📋'),
    ]

    for i, (label, value, color, icon) in enumerate(kpi_info):
        row = i // 3
        col = i % 3
        x = 0.04 + col * 0.32
        y = 0.68 - row * 0.22

        # بطاقة KPI
        card = mpatches.FancyBboxPatch(
            (x, y), 0.28, 0.18,
            boxstyle="round,pad=0.015",
            facecolor=CARD_BG, edgecolor='#E8E8E8', linewidth=1.5,
            transform=fig_kpi.transFigure
        )
        fig_kpi.patches.append(card)

        # شريط لوني علوي
        fig_kpi.patches.append(mpatches.FancyBboxPatch(
            (x, y + 0.155), 0.28, 0.025,
            boxstyle="round,pad=0.008",
            facecolor=color, edgecolor='none',
            transform=fig_kpi.transFigure
        ))

        # الأيقونة
        fig_kpi.text(x + 0.14, y + 0.125, icon, fontsize=18,
                     ha='center', va='center')

        # القيمة
        fig_kpi.text(x + 0.14, y + 0.075, value, fontsize=22,
                     fontweight='bold', color=color,
                     ha='center', va='center', fontfamily='sans-serif')

        # التسمية
        fig_kpi.text(x + 0.14, y + 0.025, label, fontsize=9,
                     color=GRAY, ha='center', va='center',
                     fontfamily='sans-serif', fontweight='bold')

    # --- Quick Insights Box ---
    insights_y = 0.05
    fig_kpi.patches.append(mpatches.FancyBboxPatch(
        (0.04, insights_y), 0.92, 0.30,
        boxstyle="round,pad=0.015",
        facecolor=CARD_BG, edgecolor='#E8E8E8', linewidth=1.5,
        transform=fig_kpi.transFigure
    ))

    fig_kpi.patches.append(mpatches.FancyBboxPatch(
        (0.04, insights_y + 0.265), 0.92, 0.035,
        boxstyle="round,pad=0.008",
        facecolor=DARK_BLUE, edgecolor='none',
        transform=fig_kpi.transFigure
    ))

    fig_kpi.text(0.5, insights_y + 0.282, '🔍  QUICK INSIGHTS',
                 fontsize=12, fontweight='bold', color='white',
                 ha='center', va='center', fontfamily='sans-serif')

    insights = [
        f"🏆  Best Selling Product:  {best_product}  (${product_summary.loc[product_summary['Product']==best_product, 'Revenue'].values[0]:,.0f} revenue)",
        f"🌍  Top Performing Region:  {best_region}  (${region_summary.loc[region_summary['Region']==best_region, 'Revenue'].values[0]:,.0f} revenue)",
        f"📅  Best Month:  {monthly_summary.loc[monthly_summary['Revenue'].idxmax(), 'Month_Name']}  (${monthly_summary['Revenue'].max():,.0f} revenue)",
        f"📉  Lowest Product:  {worst_product}  (${product_summary.loc[product_summary['Product']==worst_product, 'Revenue'].values[0]:,.0f} revenue)",
        f"📊  Average Profit per Order:  ${total_profit/total_orders:,.0f}",
    ]

    for j, insight in enumerate(insights):
        fig_kpi.text(0.08, insights_y + 0.22 - j * 0.045, insight,
                     fontsize=10, color='#2C3E50',
                     ha='left', va='center', fontfamily='sans-serif')

    plt.axis('off')
    pdf.savefig(fig_kpi, facecolor=fig_kpi.get_facecolor())
    plt.close(fig_kpi)

    # ==========================================
    # الصفحة 3: الرسوم البيانية (1 و 2)
    # ==========================================
    fig3, axes3 = plt.subplots(1, 2, figsize=(11.69, 8.27))
    fig3.patch.set_facecolor(BG_COLOR)

    # شريط العنوان
    fig3.patches.append(mpatches.FancyBboxPatch(
        (0.02, 0.91), 0.96, 0.07,
        boxstyle="round,pad=0.01",
        facecolor=DARK_BLUE, edgecolor='none',
        transform=fig3.transFigure
    ))
    fig3.text(0.5, 0.945, 'SALES ANALYSIS — PRODUCT & REGION',
              fontsize=18, fontweight='bold', color='#FFFFFF',
              ha='center', va='center', fontfamily='sans-serif')

    plt.subplots_adjust(top=0.85, bottom=0.12, left=0.08,
                        right=0.95, wspace=0.35)

    # --- رسم 1: إيرادات حسب المنتج ---
    ax1 = axes3[0]
    bars = ax1.bar(product_summary['Product'], product_summary['Revenue'],
                   color=colors_palette[:len(product_summary)],
                   edgecolor='white', linewidth=1.5, width=0.6)
    ax1.set_title('Revenue by Product', fontsize=14, fontweight='bold',
                  color=DARK_BLUE, pad=15)
    ax1.set_ylabel('Revenue ($)', fontsize=10, color=GRAY)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color('#DADADA')
    ax1.spines['bottom'].set_color('#DADADA')
    ax1.grid(axis='y', alpha=0.2, linestyle='--')
    ax1.set_facecolor('#FAFBFC')
    ax1.tick_params(colors=GRAY)
    for bar, val in zip(bars, product_summary['Revenue']):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 300,
                 f'${val:,.0f}', ha='center', va='bottom',
                 fontsize=8, fontweight='bold', color=DARK_BLUE)

    # --- رسم 2: حصة المناطق ---
    ax2 = axes3[1]
    wedges, texts, autotexts = ax2.pie(
        region_summary['Revenue'],
        labels=region_summary['Region'],
        autopct='%1.1f%%',
        colors=colors_palette[:len(region_summary)],
        startangle=90,
        pctdistance=0.8,
        wedgeprops=dict(width=0.5, edgecolor='white', linewidth=2.5)
    )
    for text in texts:
        text.set_fontsize(10)
        text.set_fontweight('bold')
        text.set_color(DARK_BLUE)
    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')
        autotext.set_color('white')
    ax2.set_title('Revenue Share by Region', fontsize=14, fontweight='bold',
                  color=DARK_BLUE, pad=15)

    # إجمالي في الوسط
    ax2.text(0, 0, f'${total_revenue:,.0f}\nTotal', ha='center', va='center',
             fontsize=10, fontweight='bold', color=DARK_BLUE)

    pdf.savefig(fig3, facecolor=fig3.get_facecolor())
    plt.close(fig3)

    # ==========================================
    # الصفحة 4: الرسوم البيانية (3 و 4)
    # ==========================================
    fig4, axes4 = plt.subplots(1, 2, figsize=(11.69, 8.27))
    fig4.patch.set_facecolor(BG_COLOR)

    # شريط العنوان
    fig4.patches.append(mpatches.FancyBboxPatch(
        (0.02, 0.91), 0.96, 0.07,
        boxstyle="round,pad=0.01",
        facecolor=DARK_BLUE, edgecolor='none',
        transform=fig4.transFigure
    ))
    fig4.text(0.5, 0.945, 'SALES ANALYSIS — TRENDS & BREAKDOWN',
              fontsize=18, fontweight='bold', color='#FFFFFF',
              ha='center', va='center', fontfamily='sans-serif')

    plt.subplots_adjust(top=0.85, bottom=0.12, left=0.08,
                        right=0.95, wspace=0.35)

    # --- رسم 3: الاتجاه الشهري ---
    ax3 = axes4[0]
    ax3.plot(monthly_summary['Month_Name'], monthly_summary['Revenue'],
             marker='o', linewidth=2.5, color=MEDIUM_BLUE, label='Revenue',
             markersize=8, markerfacecolor='white', markeredgewidth=2,
             markeredgecolor=MEDIUM_BLUE, zorder=5)
    ax3.plot(monthly_summary['Month_Name'], monthly_summary['Profit'],
             marker='s', linewidth=2.5, color=GREEN, label='Profit',
             markersize=7, markerfacecolor='white', markeredgewidth=2,
             markeredgecolor=GREEN, zorder=5)
    ax3.fill_between(monthly_summary['Month_Name'], monthly_summary['Revenue'],
                     alpha=0.08, color=MEDIUM_BLUE)
    ax3.fill_between(monthly_summary['Month_Name'], monthly_summary['Profit'],
                     alpha=0.08, color=GREEN)
    ax3.set_title('Monthly Revenue & Profit Trend', fontsize=14,
                  fontweight='bold', color=DARK_BLUE, pad=15)
    ax3.set_ylabel('Amount ($)', fontsize=10, color=GRAY)
    ax3.legend(frameon=True, fancybox=True, shadow=True, fontsize=9)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['left'].set_color('#DADADA')
    ax3.spines['bottom'].set_color('#DADADA')
    ax3.grid(axis='y', alpha=0.2, linestyle='--')
    ax3.set_facecolor('#FAFBFC')
    ax3.tick_params(colors=GRAY)

    # --- رسم 4: مقارنة الإيرادات والأرباح حسب المنتج ---
    ax4 = axes4[1]
    x_pos = np.arange(len(product_summary))
    width = 0.35
    bars1 = ax4.bar(x_pos - width/2, product_summary['Revenue'],
                    width, label='Revenue', color=MEDIUM_BLUE,
                    edgecolor='white', linewidth=1)
    bars2 = ax4.bar(x_pos + width/2, product_summary['Profit'],
                    width, label='Profit', color=GREEN,
                    edgecolor='white', linewidth=1)
    ax4.set_title('Revenue vs Profit by Product', fontsize=14,
                  fontweight='bold', color=DARK_BLUE, pad=15)
    ax4.set_ylabel('Amount ($)', fontsize=10, color=GRAY)
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels(product_summary['Product'])
    ax4.legend(frameon=True, fancybox=True, shadow=True, fontsize=9)
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['left'].set_color('#DADADA')
    ax4.spines['bottom'].set_color('#DADADA')
    ax4.grid(axis='y', alpha=0.2, linestyle='--')
    ax4.set_facecolor('#FAFBFC')
    ax4.tick_params(colors=GRAY)

    pdf.savefig(fig4, facecolor=fig4.get_facecolor())
    plt.close(fig4)

    # ==========================================
    # الصفحة 5: الجداول التفصيلية
    # ==========================================
    fig_tables = plt.figure(figsize=(11.69, 8.27))
    fig_tables.patch.set_facecolor(BG_COLOR)

    # شريط العنوان
    fig_tables.patches.append(mpatches.FancyBboxPatch(
        (0.02, 0.91), 0.96, 0.07,
        boxstyle="round,pad=0.01",
        facecolor=DARK_BLUE, edgecolor='none',
        transform=fig_tables.transFigure
    ))
    fig_tables.text(0.5, 0.945, 'DETAILED SUMMARY TABLES',
                    fontsize=18, fontweight='bold', color='#FFFFFF',
                    ha='center', va='center', fontfamily='sans-serif')

    # --- جدول المنتجات ---
    ax_t1 = fig_tables.add_axes([0.05, 0.55, 0.42, 0.30])
    ax_t1.axis('off')
    ax_t1.set_title('Summary by Product', fontsize=13, fontweight='bold',
                    color=DARK_BLUE, pad=10, loc='left')

    table_data_prod = []
    for _, row in product_summary.iterrows():
        table_data_prod.append([
            row['Product'],
            f"${row['Revenue']:,.0f}",
            f"${row['Profit']:,.0f}",
            f"{row['Orders']}"
        ])

    table1 = ax_t1.table(
        cellText=table_data_prod,
        colLabels=['Product', 'Revenue', 'Profit', 'Orders'],
        cellLoc='center',
        loc='center',
        colWidths=[0.25, 0.25, 0.25, 0.25]
    )
    table1.auto_set_font_size(False)
    table1.set_fontsize(10)
    table1.scale(1, 1.8)

    for (row, col), cell in table1.get_celld().items():
        cell.set_edgecolor('#E8E8E8')
        if row == 0:
            cell.set_facecolor(DARK_BLUE)
            cell.set_text_props(color='white', fontweight='bold')
        else:
            cell.set_facecolor('#FFFFFF' if row % 2 == 1 else '#F8F9FA')

    # --- جدول المناطق ---
    ax_t2 = fig_tables.add_axes([0.55, 0.55, 0.42, 0.30])
    ax_t2.axis('off')
    ax_t2.set_title('Summary by Region', fontsize=13, fontweight='bold',
                    color=DARK_BLUE, pad=10, loc='left')

    table_data_reg = []
    for _, row in region_summary.iterrows():
        margin = (row['Profit'] / row['Revenue'] * 100)
        table_data_reg.append([
            row['Region'],
            f"${row['Revenue']:,.0f}",
            f"${row['Profit']:,.0f}",
            f"{margin:.1f}%"
        ])

    table2 = ax_t2.table(
        cellText=table_data_reg,
        colLabels=['Region', 'Revenue', 'Profit', 'Margin %'],
        cellLoc='center',
        loc='center',
        colWidths=[0.22, 0.26, 0.26, 0.26]
    )
    table2.auto_set_font_size(False)
    table2.set_fontsize(10)
    table2.scale(1, 1.8)

    for (row, col), cell in table2.get_celld().items():
        cell.set_edgecolor('#E8E8E8')
        if row == 0:
            cell.set_facecolor(DARK_BLUE)
            cell.set_text_props(color='white', fontweight='bold')
        else:
            cell.set_facecolor('#FFFFFF' if row % 2 == 1 else '#F8F9FA')

    # --- جدول الأشهر ---
    ax_t3 = fig_tables.add_axes([0.15, 0.07, 0.70, 0.40])
    ax_t3.axis('off')
    ax_t3.set_title('Monthly Performance Summary', fontsize=13,
                    fontweight='bold', color=DARK_BLUE, pad=10, loc='left')

    table_data_month = []
    for _, row in monthly_summary.iterrows():
        margin_m = (row['Profit'] / row['Revenue'] * 100)
        table_data_month.append([
            row['Month_Name'],
            f"${row['Revenue']:,.0f}",
            f"${row['Profit']:,.0f}",
            f"{row['Orders']}",
            f"${row['Revenue']/row['Orders']:,.0f}",
            f"{margin_m:.1f}%"
        ])

    table3 = ax_t3.table(
        cellText=table_data_month,
        colLabels=['Month', 'Revenue', 'Profit',
                   'Orders', 'Avg Order', 'Margin %'],
        cellLoc='center',
        loc='center',
        colWidths=[0.14, 0.18, 0.18, 0.14, 0.18, 0.18]
    )
    table3.auto_set_font_size(False)
    table3.set_fontsize(10)
    table3.scale(1, 1.6)

    for (row, col), cell in table3.get_celld().items():
        cell.set_edgecolor('#E8E8E8')
        if row == 0:
            cell.set_facecolor(DARK_BLUE)
            cell.set_text_props(color='white', fontweight='bold')
        else:
            cell.set_facecolor('#FFFFFF' if row % 2 == 1 else '#F8F9FA')

    pdf.savefig(fig_tables, facecolor=fig_tables.get_facecolor())
    plt.close(fig_tables)

    # ==========================================
    # الصفحة 6: الخاتمة
    # ==========================================
    fig_end = plt.figure(figsize=(11.69, 8.27))
    fig_end.patch.set_facecolor(DARK_BLUE)

    fig_end.text(0.5, 0.65, 'Thank You', fontsize=42,
                 fontweight='bold', color='white',
                 ha='center', va='center', fontfamily='sans-serif')

    fig_end.patches.append(mpatches.FancyBboxPatch(
        (0.25, 0.56), 0.50, 0.005,
        boxstyle="round,pad=0.002",
        facecolor=GOLD, edgecolor='none',
        transform=fig_end.transFigure
    ))

    fig_end.text(0.5, 0.48, 'Sales Dashboard Report', fontsize=18,
                 color='#BDC3C7', ha='center', va='center',
                 fontfamily='sans-serif', style='italic')

    fig_end.text(0.5, 0.38, f'Period: Jan 2024 — Jul 2024', fontsize=14,
                 color='#7F8C8D', ha='center', va='center',
                 fontfamily='sans-serif')

    fig_end.text(0.5, 0.25,
                 f'Revenue: ${total_revenue:,.0f}   |   '
                 f'Profit: ${total_profit:,.0f}   |   '
                 f'Margin: {profit_margin:.1f}%',
                 fontsize=13, color=GOLD, ha='center', va='center',
                 fontfamily='sans-serif', fontweight='bold')

    fig_end.text(0.5, 0.10, 'Generated using Python  •  pandas  •  matplotlib',
                 fontsize=9, color='#566573', ha='center', va='center',
                 fontfamily='sans-serif')

    plt.axis('off')
    pdf.savefig(fig_end, facecolor=fig_end.get_facecolor())
    plt.close(fig_end)

# ============================================
print("=" * 60)
print(f"✅  تم إنشاء ملف PDF بنجاح: {pdf_file}")
print("=" * 60)
print(f"\nالتقرير يحتوي على {6} صفحات:")
print(f"  📄 صفحة 1: غلاف التقرير")
print(f"  📄 صفحة 2: مؤشرات الأداء (6 KPIs) + رؤى سريعة")
print(f"  📄 صفحة 3: إيرادات المنتجات + حصص المناطق")
print(f"  📄 صفحة 4: الاتجاه الشهري + مقارنة الإيرادات/الأرباح")
print(f"  📄 صفحة 5: جداول تفصيلية (منتجات، مناطق، أشهر)")
print(f"  📄 صفحة 6: صفحة الختام")
print(f"\n🎉 افتح الملف '{pdf_file}' للاطلاع على التقرير!")
by

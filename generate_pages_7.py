PAGES["partner.html"] = {
    "title": "Partner With Us",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "header__nav-link--active",
    "impact_active": "",
    "contact_active": "",
    "content": """
    <section class="inner-hero watermark-bg" style="background-color: var(--ivory); padding: 180px 0 80px;">
      <div class="container text-center reveal">
        <h1 class="heading-display">Partner With Us</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Collaborate with Ananth Sarth Seva Foundation to create scalable, tech-enabled social change.</p>
      </div>
    </section>
    
    <section class="section" style="background-color: var(--white);">
      <div class="container reveal">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <h2 class="heading-md">Why Partner With Us?</h2>
            <p style="margin-top: 16px;">We believe that solving complex rural challenges requires cross-sector collaboration. We partner with CSR initiatives, tech innovators, academic institutions, and government bodies to bring the Root-to-Rise model to life.</p>
        </div>
        
        <div class="features-grid" style="margin-top: 56px;">
            """ + build_3d_card("Corporate Social Responsibility (CSR)", "Deploy your CSR funds into traceable, high-impact, and sustainable community projects.", ICONS["briefcase"]) + """
            """ + build_3d_card("Technology Providers", "Provide software, hardware, and digital tools to empower rural innovators.", ICONS["cpu"]) + """
            """ + build_3d_card("Academic Institutions", "Collaborate on research, skill-building curriculums, and student exchange programs.", ICONS["library"]) + """
        </div>
        
        <div style="text-align: center; margin-top: 64px;">
            <p class="text-md">Ready to explore a partnership?</p>
            <a href="contact.html" class="btn btn--primary" style="margin-top: 24px;">Get in Touch</a>
        </div>
      </div>
    </section>
"""
}

def generate_legal_page(title, content):
    return f"""
    <section class="inner-hero" style="background-color: var(--royal-blue); color: white; padding: 160px 0 60px;">
      <div class="container text-center reveal">
        <h1 class="heading-display text-white">{title}</h1>
      </div>
    </section>
    <section class="section" style="background-color: var(--white);">
      <div class="container reveal" style="max-width: 800px; font-size: 16px; line-height: 1.8;">
        {content}
      </div>
    </section>
"""

PAGES["privacy.html"] = {
    "title": "Privacy Policy",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Privacy Policy", """
        <h2>1. Introduction</h2>
        <p>Ananth Sarth Seva Foundation is committed to protecting your privacy and ensuring the security of your personal information. This Privacy Policy outlines how we collect, use, disclose, and protect the information you provide when using our website and services.</p>
        
        <h2>2. Information We Collect</h2>
        <p>We may collect personal information such as your name, email address, phone number, mailing address, and payment information when you make a donation, volunteer, or contact us. We also collect non-personal data such as browser type, IP address, and pages visited through cookies and analytics tools.</p>
        
        <h2>3. How We Use Your Information</h2>
        <p>Your information is used to process donations, issue receipts (including 80G tax exemption certificates), respond to inquiries, send newsletters and updates (if opted in), and improve our website and services.</p>
        
        <h2>4. Data Sharing and Disclosure</h2>
        <p>We do not sell, trade, or rent your personal information to third parties. We may share necessary information with trusted service providers (e.g., payment gateways) solely for processing transactions or operating our website, under strict confidentiality agreements. We may also disclose information if required by law.</p>
        
        <h2>5. Data Security</h2>
        <p>We implement appropriate technical and organizational measures to safeguard your data against unauthorized access, alteration, disclosure, or destruction. However, no internet transmission is completely secure.</p>
        
        <h2>6. Your Rights</h2>
        <p>You have the right to access, correct, or request deletion of your personal data. To exercise these rights, please contact our Grievance Officer.</p>
        
        <h2>7. Contact Information</h2>
        <p>Grievance Officer: [CLIENT: GRIEVANCE OFFICER NAME/CONTACT]<br>Email: [CLIENT: OFFICIAL EMAIL]<br>Address: [CLIENT: REGISTERED OFFICE ADDRESS]</p>
    """)
}

PAGES["terms.html"] = {
    "title": "Terms of Use",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Terms of Use", """
        <h2>1. Acceptance of Terms</h2>
        <p>By accessing and using the Ananth Sarth Seva Foundation website, you agree to comply with and be bound by these Terms of Use. If you do not agree to these terms, please refrain from using our website.</p>
        
        <h2>2. Use of Content</h2>
        <p>All content on this website, including text, graphics, logos, and images, is the property of Ananth Sarth Seva Foundation and is protected by copyright laws. You may use this content for personal, non-commercial purposes only. Any other use requires our prior written consent.</p>
        
        <h2>3. User Conduct</h2>
        <p>You agree to use our website for lawful purposes only and in a manner that does not infringe on the rights of, or restrict the use of the site by, any third party. Harassment, defamatory content, and unauthorized access are strictly prohibited.</p>
        
        <h2>4. Donations and Payments</h2>
        <p>All donations made through our website are subject to our Donation and Refund Policies. By making a payment, you confirm that you are authorized to use the provided payment method.</p>
        
        <h2>5. Disclaimer of Warranties</h2>
        <p>The information on this website is provided "as is" without any representations or warranties, express or implied. We do not guarantee that the website will be error-free or uninterrupted.</p>
        
        <h2>6. Limitation of Liability</h2>
        <p>Ananth Sarth Seva Foundation shall not be liable for any direct, indirect, incidental, or consequential damages arising out of your use of or inability to use the website.</p>
        
        <h2>7. Governing Law</h2>
        <p>These terms shall be governed by and construed in accordance with the laws of India. Any disputes shall be subject to the exclusive jurisdiction of the courts in the state where our registered office is located.</p>
    """)
}

PAGES["donation-policy.html"] = {
    "title": "Donation Policy",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Donation Policy", """
        <h2>1. Purpose of Donations</h2>
        <p>Donations received by Ananth Sarth Seva Foundation are utilized to fund our core programs: Holistic Learning, Women's Equity, Resilient Communities, Inclusive Wellness, Climate Resilience, and Eco-Conservation.</p>
        
        <h2>2. Donation Processing</h2>
        <p>We accept donations via secure online payment gateways, bank transfers, and cheques. All transactions are processed in Indian Rupees (INR) unless otherwise specified.</p>
        
        <h2>3. Tax Exemption (80G)</h2>
        <p>Ananth Sarth Seva Foundation is registered under Section 80G of the Income Tax Act, 1961. Donors are eligible for tax exemption on their contributions as per the prevailing laws. Ensure you provide your PAN details during the donation process to receive a valid 80G receipt.</p>
        
        <h2>4. Receipts</h2>
        <p>A formal receipt and an 80G certificate will be issued for all valid donations. Electronic receipts are typically sent within a few business days following successful payment realization.</p>
        
        <h2>5. Foreign Contributions</h2>
        <p>Currently, we accept foreign contributions only in compliance with the Foreign Contribution (Regulation) Act (FCRA). Please contact us directly if you wish to make an international donation.</p>
    """)
}

PAGES["refund-policy.html"] = {
    "title": "Refund Policy",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Refund Policy", """
        <h2>1. General Policy</h2>
        <p>Ananth Sarth Seva Foundation treats all donations as voluntary contributions. As a general rule, donations once made cannot be refunded.</p>
        
        <h2>2. Exceptional Circumstances for Refund</h2>
        <p>We may consider refund requests in exceptional circumstances, such as:</p>
        <ul>
            <li>Duplicate transactions due to technical errors.</li>
            <li>Fraudulent use of a credit/debit card.</li>
        </ul>
        
        <h2>3. Requesting a Refund</h2>
        <p>If you believe you are entitled to a refund based on the above criteria, you must submit a written request to [CLIENT: OFFICIAL EMAIL] within 7 days of the transaction date. Your request must include:</p>
        <ul>
            <li>Date of Donation</li>
            <li>Donation Amount</li>
            <li>Transaction ID or Reference Number</li>
            <li>Reason for the refund request</li>
        </ul>
        
        <h2>4. Processing</h2>
        <p>All refund decisions are at the sole discretion of the Foundation's management. If approved, refunds will be processed and credited back to the original source of payment within 10-15 business days.</p>
    """)
}

PAGES["accessibility.html"] = {
    "title": "Accessibility Statement",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Accessibility Statement", """
        <h2>Our Commitment</h2>
        <p>Ananth Sarth Seva Foundation is committed to ensuring digital accessibility for people with disabilities. We are continually improving the user experience for everyone and applying the relevant accessibility standards.</p>
        
        <h2>Conformance Status</h2>
        <p>The Web Content Accessibility Guidelines (WCAG) defines requirements for designers and developers to improve accessibility for people with disabilities. We strive to conform to WCAG 2.1 level AA standards.</p>
        
        <h2>Key Accessibility Features</h2>
        <ul>
            <li><strong>Clear Hierarchy:</strong> Use of semantic HTML and clear heading structures.</li>
            <li><strong>Keyboard Navigation:</strong> Our site is designed to be navigable using a keyboard.</li>
            <li><strong>Color Contrast:</strong> Text and background colors are chosen to ensure sufficient contrast.</li>
            <li><strong>Alternative Text:</strong> Informative images include descriptive alt text.</li>
        </ul>
        
        <h2>Feedback</h2>
        <p>We welcome your feedback on the accessibility of our website. If you encounter accessibility barriers, please let us know at [CLIENT: OFFICIAL EMAIL]. We try to respond to feedback within 5 business days.</p>
    """)
}

# GENERATION SCRIPT
def generate_pages():
    for filepath, data in PAGES.items():
        html_content = HEADER_TEMPLATE.format(
            title=data["title"],
            root_path=data["root_path"],
            about_active=data["about_active"],
            programs_active=data["programs_active"],
            involved_active=data["involved_active"],
            impact_active=data["impact_active"],
            contact_active=data["contact_active"]
        )
        html_content += data["content"]
        html_content += FOOTER_TEMPLATE.format(
            root_path=data["root_path"]
        )
        
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {filepath}")
    print("All pages generated successfully!")

if __name__ == "__main__":
    generate_pages()

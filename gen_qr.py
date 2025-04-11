import qrcode
import os

# Base URL to prepend to routes
BASE_URL = "https://qrazy-hunt.vercel.app"

# Routes and their associated HTML templates
routes = [
    # Main route
    ("", "index.html"),
    
    # Clue routes
    ("/clue1_sd8f987sdf76876sdf", "clue1.html"),
    ("/clue2_s89d7f87sdf67876vv", "clue2.html"),
    ("/clue3_poi45o6i4opi56pip4o56", "clue3.html"),
    ("/clue4_mbnwb45mnbm4b5m3nb451", "clue4.html"),
    ("/clue5_0x90s9df0s9df989sdf", "clue5.html"),
    ("/clue6_m2m3n42n34mn23m4nm", "clue6.html"),
    ("/clue7_kj2k3j4234jk23h4kjhj2", "clue7.html"),
    
    # Final clue routes
    ("/final_clue_9s0d890s809f8s90d8f", "final-clue-1.html"),
    ("/final_clue_mk23n4j23n4k2n3kj42j4545", "final-clue-2.html"),
    ("/final_clue_kh4k5h34kj5h34jk5hkjhk34", "final-clue-3.html"),
    ("/final_clue_sd098fs90d87f09sdf", "final-clue-4.html"),
    ("/final_clue_asd098a0s98da90s8d", "final-clue-5.html"),
    ("/final_clue_2i3l4kj2l3j4l23j4l", "final-clue-6.html"),
    ("/final_clue_2klh34kj2h34jkh23", "final-clue-7.html"),
    ("/final_clue_sd098f09s8df09sd8f809sdf", "final-clue-8.html"),
]

# Create output directory if it doesn't exist
output_dir = "qr_codes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate QR codes for each route
for route, html_file in routes:
    # Create the full URL
    full_url = f"{BASE_URL}{route}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(full_url)
    qr.make(fit=True)
    
    # Create an image from the QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Output filename based on the HTML file name (without .html extension)
    output_filename = os.path.join(output_dir, html_file.replace(".html", ".png"))
    
    # Save the image
    img.save(output_filename)
    print(f"Generated QR code for {html_file} at {output_filename}")

print(f"\nAll QR codes have been generated in the '{output_dir}' directory.")
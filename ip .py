from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Create the banner
def create_banner():
    top_border = "/" * 80
    bottom_border = "\\" * 80

    # Program name and styling
    program_name = f"{Fore.RED}ip address checker  "
    team_name = f"{Fore.GREEN}ip checker !!"
    developer_name = f"{Fore.YELLOW}himansu pal"
    github_link = f"{Fore.CYAN}https://github.com/himansu-pal419845"

    # Combine all parts of the banner
    banner = f"""
{top_border}
    <Program>   {program_name}   </Program>
    <Team>   {team_name}   </Team>
    <Developer>   {developer_name}   </Developer>
    <GitHub>   {github_link}   </GitHub>
{bottom_border}
"""
    return banner

# Print the banner
print(create_banner())



import requests

def get_ip_location(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    if response.status_code == 200:
        data = response.json()
        location = data.get("loc", "Location not found")
        city = data.get("city", "City not found")
        region = data.get("region", "Region not found")
        country = data.get("country", "Country not found")
        return f"IP: {ip}\nLocation: {location} (Lat, Long)\nCity: {city}\nRegion: {region}\nCountry: {country}"
    else:
        return "Could not retrieve location information."

# Example Usage
ip_address =input("enter your ip address:")   # Replace with target IP
print(get_ip_location(ip_address))
#Must install beutiful soup the web scraper we are using
#Must install requests a socket library
import requests
# from bs4 import BeautifulSoup
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
import time
#Fake Cookies To Avoid Bot Detection
walmartHeader = {
  'authority': 'www.walmart.com',
  'accept': 'application/json',
  'accept-language': 'en-US',
  'content-type': 'application/json',
  'cookie': 'ACID=7a8e99e1-134b-4fe4-9eb3-f4c71de79e9d; hasACID=true; _m=9; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjE4NzAiLCJ0aW1lc3RhbXAiOjE3MDgyMDM2NDk2OTEsInNlbGVjdGlvblR5cGUiOiJMU19TRUxFQ1RFRCIsInNlbGVjdGlvblNvdXJjZSI6IklQX1NOSUZGRURfQllfTFMifSwic2hpcHBpbmdBZGRyZXNzIjp7InRpbWVzdGFtcCI6MTcwODIwMzY0OTY5MSwidHlwZSI6InBhcnRpYWwtbG9jYXRpb24iLCJnaWZ0QWRkcmVzcyI6ZmFsc2UsInBvc3RhbENvZGUiOiI5OTE2NCIsImNpdHkiOiJQdWxsbWFuIiwic3RhdGUiOiJXQSIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIxODcwIiwidHlwZSI6IkRFTElWRVJZIiwidGltZXN0YW1wIjoxNzA4MTkzMDY5MDc0LCJzZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJzZWxlY3Rpb25Tb3VyY2UiOiJJUF9TTklGRkVEX0JZX0xTIn1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE3MDgyMDM2NDk2OTEsImJhc2UiOiI5OTE2NCJ9LCJtcCI6W10sInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo3YThlOTllMS0xMzRiLTRmZTQtOWViMy1mNGM3MWRlNzllOWQifQ%3D%3D; userAppVersion=us-web-1.117.0-a9e2f78a3d8f5ecd28bab89ca6646fa61af3a12b-0215; abqme=false; vtc=UfxjOGpqOZLcKKnCK3-nD0; _pxhd=eb69add58e09c9c9204ec709f80b8cc71d37f431884f43332d3bc62e0daaa3ae:a0e69de2-cdd7-11ee-8f70-d21949a33ed6; TBV=7; pxcts=408d32fb-cde7-11ee-b689-35daa94a6eef; _pxvid=a0e69de2-cdd7-11ee-8f70-d21949a33ed6; _astc=65f3484ec7aafc132d6e0ced377777b8; dimensionData=945; adblocked=true; auth=MTAyOTYyMDE4N8ojR439eoTEkebZaksCwESZ6CTVJhUZ0Y9qj4jmyUSEg7N%2FK7CGMb08j0uWgQvzbIDWe4EDOPdr8FfjS%2BEKTBKUR8dOKUlnfPG5Iyy%2BlIZjz16rTRULULUvxaBVIdlU767wuZloTfhm7Wk2Kcjygiq0nmGVz3wI1IrcfVbuZ158NmOt2rpCXYsRQqA5aVVcCY%2BYk8SrdX95dOf53BfT2KrdoSO98qgr7xSj2SyDszcUMk70P8glgOEpLOprhDfMJ0tmvH1FCaN9tZDh4SCrHaaW7jUx3dJnJVD%2BP75VZDd4ccaWCOQy7GSqX7EDICBj5EZ4ORHY9Ux%2BLaidBpwGrX8GbWN0erMLACSfX7lLJj%2BxT45vyFfMWEFaiEZTVgO1qCDr51IG7XrbzNfMRoW7NpE5WBBdZBCyKnCQAR7o6eg%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIxODcwIiwiZGlzcGxheU5hbWUiOiJQdWxsbWFuIFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk5MTYzIiwiYWRkcmVzc0xpbmUxIjoiMTY5MCBTZSBIYXJ2ZXN0IERyIiwiY2l0eSI6IlB1bGxtYW4iLCJzdGF0ZSI6IldBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5OTE2My02MDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjo0Ni43MTIwNDQsImxvbmdpdHVkZSI6LTExNy4xNzU2Mjd9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIxODcwIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9JTlNUT1JFIl0sInNlbGVjdGlvblR5cGUiOiJMU19TRUxFQ1RFRCJ9XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjo0Ni43Mjk2LCJsb25naXR1ZGUiOi0xMTcuMTUyOCwicG9zdGFsQ29kZSI6Ijk5MTY0IiwiY2l0eSI6IlB1bGxtYW4iLCJzdGF0ZSI6IldBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2UsInRpbWVab25lIjoiQW1lcmljYS9Mb3NfQW5nZWxlcyJ9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjE4NzAiLCJkaXNwbGF5TmFtZSI6IlB1bGxtYW4gU3VwZXJjZW50ZXIiLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMTg3MCIsImRpc3BsYXlOYW1lIjoiUHVsbG1hbiBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5OTE2MyIsImFkZHJlc3NMaW5lMSI6IjE2OTAgU2UgSGFydmVzdCBEciIsImNpdHkiOiJQdWxsbWFuIiwic3RhdGUiOiJXQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTkxNjMtNjAwMCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6NDYuNzEyMDQ0LCJsb25naXR1ZGUiOi0xMTcuMTc1NjI3fSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiMTg3MCIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXSwic2VsZWN0aW9uVHlwZSI6IkxTX1NFTEVDVEVEIn0sInJlZnJlc2hBdCI6MTcwODIyNDkyMDMzOCwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjdhOGU5OWUxLTEzNGItNGZlNC05ZWIzLWY0YzcxZGU3OWU5ZCJ9; assortmentStoreId=1870; hasLocData=1; bstc=UUM6Ya0scgysrF88-5hLZM; mobileweb=0; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=03J8W|1B9s0|26RfV|BENcO|CoXWr|EpRu_|IWB6I|LYm-g|OPuxL|RmLSK|Su_cI|U6WcV|VFqiY|_0DJU|aDEYa|cZcLX|cf8cl|f1Vss|fdm-7|j21L4|jZwzS|k6zHI|kQtYd|kWt1n|nEGGp|vD0Mt|wqem2|xXAc_|ynGB1; exp-ck=03J8W11B9s0126RfV2BENcO1CoXWr1EpRu_1IWB6I1OPuxL3RmLSK1U6WcV1VFqiY1_0DJU1aDEYa1cZcLX1f1Vss5fdm-71j21L41jZwzS1k6zHI1nEGGp1wqem21ynGB11; xptc=assortmentStoreId%2B1870; xpm=1%2B1708221320%2BUfxjOGpqOZLcKKnCK3-nD0~%2B0; akavpau_p1=1708222008~id=ebac694f8668994b7a22cfc991cd08b8; AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1708221431192; bm_mi=6534F113EBED0C8976F96754F41C02CC~YAAQLBM2F767AYaNAQAAlYLuuRaoRoiobEC1MbBckegh92IQ+gCPBV+YjzTWGvo0Mf0SoNSlMPm25SETlNlNhLaWDXVPgAVTo1K3UgNQf3XFrVzYh4uAPf9mcEGANrd3ne6uH6X8kBNJ061RzhKwtEaK5LcLYh1j+R/5oJq7KWxqL4vGfIdM5ymVEOT6p6QWpvRodude9ybs7t/Z4aYKKfkG5KDlY1QAhVCYVxu4LwYYBv4PmoJE7bnqtwwHIQjMQtop1wIJ6DPlHOhZkq4n40YXYdDhSlAb1qfU+Gp1R5XQwrBCP4dBIUmPR4OtjcHuI5Zu5m1kRwnPjMFR~1; bm_sv=1F5106827A678CCBCB402F94AA5582DD~YAAQLBM2F9C7AYaNAQAAuonuuRaeStczmEkG7nti8LS6aHj7gxcrVdxXB7VnkR38D4XD6d20zlFUOGWk4no9OSYT2jl24k2rtAXlEMg4M111GBeKj7wwf2BuY4hpiPYF6Dj9tUefZDWGeifUVkryZyqiiGa/JNGBgRlmbjbMZUfGSxh6TplPGw8Y8zQLdW0sXnlNzuDn88wCRsqyMhV9m/vo8mDtrYeGEOjaRLx2VkXPLejaQTXZan//Vv/8uzQSB0I=~1; ak_bmsc=A898B33B095CBEF1F1BE15C5929C09D1~000000000000000000000000000000~YAAQLBM2FzS8AYaNAQAA88XuuRb3OrdpSswl0TUmc9SLHuyDVJVrxm87N5Pg1TZKpYpSMPOu2Ht1ifyZEyTKeo3i9TMj6kYklIQhLNZjS71fVkrFujSFRuRFTfRnW/ZU4m2XEoJEQlAn9002SArZ249lt8UvgIsY4a9N4rCIVsj9sGTOdirymuFI8uu5RZO3rtFr2fbaMRtEGMpzj8JIXNj3sbLfqHsKKdX05daR6CaEM24gSfpG8E6XQmN2vWZOV5S6ExQU2kgk2Yn7H1is4Xmb51GGbhgOBLKhbNX4kQeliMr78AHeJqoaRGMKKTDzHOYejxeDwhOsoR7oQO/V2+oqtdcSzn/yC/RTCOIHmis0wpKxVjGNXQEvfK3SUV+YDTATSZOxM1k/vlIHN7MS30wheCcwaSluNXegicsWXcoYecbQ87y45jkzbck=; xptwj=qq:2ce998ada32c1de46a6f:n6OYe8zOXEkgAFhHiQtcCkRCBQJttA8QCgxE4MvDDyEPH5FjRxp9Tw2h04wlJytgmf2Rj34lUL0g9+NzicnhEGgsz2Hr8HK/9VZl7Dpg8yb6JJpi8s1IrhHzILg3m8eOnY1DlxiwPut0Y0e0IZS8Y7JIvFOBOGQ=; akavpau_p2=1708222663~id=87cf275a0a475e4a11e66c9e50a431f5; com.wm.reflector="reflectorid:0000000000000000000000^@lastupd:1708222067000^@firstcreate:1708203649656"; xptwg=2850415796:F95E37EECB6668:272FBDB:A3DFBCD3:DED0A089:45B2FB32:; TS012768cf=014c93cc48f33c111e939e666dcddf0943e9a637f20600a7358113b35290645356b5473d38227d3f95ca5ee0ded065fce3e6514b5f; TS01a90220=014c93cc48f33c111e939e666dcddf0943e9a637f20600a7358113b35290645356b5473d38227d3f95ca5ee0ded065fce3e6514b5f; TS2a5e0c5c027=08f6845631ab20003dc06e7e640e081352c2922ed0e1dc25c2c58215f593d955525b9000dfd3363f08246b23b91130004eaf387378144bc373354fd66b45fce06568ac23a210a8be5d2f1d279311ebdc331e3decc46411a509ded20f7bda203c; TS01a90220=010a503cbddebd86db0b28ad9eeff72f96e35055cf7d02e01901e54f6e0050e4644cb79f084b7375c130a312ab1eee9bcf5d3d496f; _m=9; bstc=UUM6Ya0scgysrF88-5hLZM; exp-ck=03J8W11B9s0126RfV2BENcO1CoXWr1EpRu_1IWB6I1OPuxL3RmLSK1U6WcV1VFqiY1_0DJU1aDEYa1cZcLX1f1Vss5fdm-71j21L41jZwzS1k6zHI1nEGGp1wqem21ynGB11; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjE4NzAiLCJ0aW1lc3RhbXAiOjE3MDgyMDM2NDk2OTEsInNlbGVjdGlvblR5cGUiOiJMU19TRUxFQ1RFRCIsInNlbGVjdGlvblNvdXJjZSI6IklQX1NOSUZGRURfQllfTFMifSwic2hpcHBpbmdBZGRyZXNzIjp7InRpbWVzdGFtcCI6MTcwODIwMzY0OTY5MSwidHlwZSI6InBhcnRpYWwtbG9jYXRpb24iLCJnaWZ0QWRkcmVzcyI6ZmFsc2UsInBvc3RhbENvZGUiOiI5OTE2NCIsImNpdHkiOiJQdWxsbWFuIiwic3RhdGUiOiJXQSIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIxODcwIiwidHlwZSI6IkRFTElWRVJZIiwidGltZXN0YW1wIjoxNzA4MTkzMDY5MDc0LCJzZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJzZWxlY3Rpb25Tb3VyY2UiOiJJUF9TTklGRkVEX0JZX0xTIn1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE3MDgyMDM2NDk2OTEsImJhc2UiOiI5OTE2NCJ9LCJtcCI6W10sInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo3YThlOTllMS0xMzRiLTRmZTQtOWViMy1mNGM3MWRlNzllOWQifQ%3D%3D; mobileweb=0; vtc=UfxjOGpqOZLcKKnCK3-nD0; xpa=03J8W|1B9s0|26RfV|BENcO|CoXWr|EpRu_|IWB6I|LYm-g|OPuxL|RmLSK|Su_cI|U6WcV|VFqiY|_0DJU|aDEYa|cZcLX|cf8cl|f1Vss|fdm-7|j21L4|jZwzS|k6zHI|kQtYd|kWt1n|nEGGp|vD0Mt|wqem2|xXAc_|ynGB1; xpm=0%2B1708225047%2BUfxjOGpqOZLcKKnCK3-nD0~%2B0; xptc=assortmentStoreId%2B1870; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xptwg=2880037130:E15E56C56CF848:236A41A:A5E4373C:B654F3F4:15BA4DA1:; xptwj=qq:7c8cd44b5aa065d409d4:t1vqWotmvsR9qqdWPrfvOgcPkLHIuEHoAj6vRVHuEr9799RWwkR+NzVA3MZCeyTkjv2IFnxQ86lsarfd5L+Va1/MkaRxx++KQatKGMtindqiG/Mr86Cf+8vCdL9vL5w3vFQ/zQ14IfcInkl/vdS8ez/9CNlHHoI=; TS012768cf=010a503cbddebd86db0b28ad9eeff72f96e35055cf7d02e01901e54f6e0050e4644cb79f084b7375c130a312ab1eee9bcf5d3d496f; TS2a5e0c5c027=0876775b91ab2000384f3ce66809ffdd8a24dae03bce866b59e0461a0794451285ac1c8df9301b7908d8e142e2113000e62c5c391a4497e33e961ae86d6f55710b0c6a4448943b1bc9678fb19c31678708cd74a11e2371560469363c41275fb9; abqme=false; akavpau_p2=1708225648~id=00560416d8fa8a69b3ad65894f7a5f3d; assortmentStoreId=1870; hasLocData=1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIxODcwIiwiZGlzcGxheU5hbWUiOiJQdWxsbWFuIFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk5MTYzIiwiYWRkcmVzc0xpbmUxIjoiMTY5MCBTZSBIYXJ2ZXN0IERyIiwiY2l0eSI6IlB1bGxtYW4iLCJzdGF0ZSI6IldBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5OTE2My02MDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjo0Ni43MTIwNDQsImxvbmdpdHVkZSI6LTExNy4xNzU2Mjd9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIxODcwIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9JTlNUT1JFIl0sInNlbGVjdGlvblR5cGUiOiJMU19TRUxFQ1RFRCJ9XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjo0Ni43Mjk2LCJsb25naXR1ZGUiOi0xMTcuMTUyOCwicG9zdGFsQ29kZSI6Ijk5MTY0IiwiY2l0eSI6IlB1bGxtYW4iLCJzdGF0ZSI6IldBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2UsInRpbWVab25lIjoiQW1lcmljYS9Mb3NfQW5nZWxlcyJ9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjE4NzAiLCJkaXNwbGF5TmFtZSI6IlB1bGxtYW4gU3VwZXJjZW50ZXIiLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMTg3MCIsImRpc3BsYXlOYW1lIjoiUHVsbG1hbiBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5OTE2MyIsImFkZHJlc3NMaW5lMSI6IjE2OTAgU2UgSGFydmVzdCBEciIsImNpdHkiOiJQdWxsbWFuIiwic3RhdGUiOiJXQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTkxNjMtNjAwMCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6NDYuNzEyMDQ0LCJsb25naXR1ZGUiOi0xMTcuMTc1NjI3fSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiMTg3MCIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXSwic2VsZWN0aW9uVHlwZSI6IkxTX1NFTEVDVEVEIn0sInJlZnJlc2hBdCI6MTcwODIyODY0Nzk4OCwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjdhOGU5OWUxLTEzNGItNGZlNC05ZWIzLWY0YzcxZGU3OWU5ZCJ9; userAppVersion=us-web-1.117.0-a9e2f78a3d8f5ecd28bab89ca6646fa61af3a12b-0215',
  'downlink': '10',
  'dpr': '1',
  'referer': 'https://www.walmart.com/browse/all-food/976759_9638107?page=2&affinityOverride=default',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-ffa0a826d0e91fd7de3e0031934a0960-527b23556119dc46-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'wm_mp': 'true',
  'wm_qos.correlation_id': 'T_zlVZym0SmAp8eun_iGFe6LZ-hWoiamAHPC',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-US',
  'x-o-correlation-id': 'T_zlVZym0SmAp8eun_iGFe6LZ-hWoiamAHPC',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'us-web-1.117.0-a9e2f78a3d8f5ecd28bab89ca6646fa61af3a12b-0215',
  'x-o-segment': 'oaoh'
}

safewayHeader = {
  'authority': 'www.safeway.com',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'akacd_PR-bg-www-prod-safeway=3885649709~rv=48~id=38fafd9bfba78a34b2b008e873b6b800; visid_incap_1610353=QME3z2BYT4SY806SoFjMPi0E0WUAAAAAQUIPAAAAAABrBK5GUR84iLi6sYB9eTFp; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; ECommBanner=safeway; ECommSignInCount=0; SAFEWAY_MODAL_LINK=; at_check=true; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2299163%22%2C%22banner%22%3A%22safeway%22%2C%22siteType%22%3A%22C%22%2C%22customerType%22%3A%22%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2299163%22%2C%22storeId%22%3A%222639%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2299163%22%2C%22storeId%22%3A%222639%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2299163%22%2C%22banner%22%3A%22safeway%22%2C%22siteType%22%3A%22C%22%2C%22customerType%22%3A%22%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2299163%22%2C%22storeId%22%3A%222639%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2299163%22%2C%22storeId%22%3A%222639%22%7D%7D%7D; OptanonAlertBoxClosed=2024-02-17T20:55:59.689Z; incap_ses_1566_1610353=of1OdlrtqWfBn5EQUI27FY9j0WUAAAAA0LhONRxWnoNHyTFGL9Ws1w==; incap_ses_731_1610353=UxVoCNn/ylGJRPzdPAslCsp10WUAAAAAzdnd1ceX3CPybj+VqlVUNw==; nlbi_1610353=olo5S62UOBXHx16/6eNT2gAAAAB++VFbOYxtXDw0Qi4YoOHx; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2299163%22%2C%22storeId%22%3A%222639%22%2C%22preference%22%3A%22J4U%22%7D; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2299163%22%2C%22banner%22%3A%22safeway%22%2C%22preference%22%3A%22J4U%22%2C%22Selection%22%3A%22user%22%2C%22userData%22%3A%7B%7D%2C%22grsSessionId%22%3A%22426043d6-6db5-4713-874b-7dbee2df9e7d%22%2C%22siteType%22%3A%22C%22%2C%22customerType%22%3A%22%22%7D%2C%22J4U%22%3A%7B%22storeId%22%3A%222639%22%2C%22zipcode%22%3A%2299163%22%2C%22userData%22%3A%7B%7D%7D%2C%22SHOP%22%3A%7B%22storeId%22%3A%222639%22%2C%22zipcode%22%3A%2299163%22%2C%22userData%22%3A%7B%7D%7D%7D%7D; reese84=3:apNigTE7XIiOexWLxLKWrQ==:BLCAxkCahreSPAbhkoet+QsNnMl1cxBJzto0VADEoTqOoXc2hU9hLuRO3glpr6lyQsF9yG91h1jL9Qofxgy86Pcil7Ga0Bxw8ZwMeCx8Pg9NvzZjgbm2vKsB7NL0DIeknlk0NXgr1XkwYxIObpr10E4L9n/gF8ICgrXPUeiKHJIQLSyBqAE0hgD5nAKC+FOjeL20+c1Qkrk2OvJdY9vVl4ZTtDM/tLtqsXDWxur9SPXyXw8IpiR1GvjF/Xyv+lBtJA+uYR1hUryFWdu1R93D9cyiNReCz2FlSSqOHl+hGjaFj5XKPlJ6ukNNTNNh450DIxfwlipNpzRGBJj8wbFtRG25g7bhbo3JFZgrSp6ZczKVhForM1SyoBxgeYKuEMkV8Z61DR+PsY2z8T3zUIWAcWZZrDqhijL0i581Nd4H+RRqSyCDgNnIPa6m+pprh+4xw+14qspuYhsL4cgpHy0GyHlmxYOLnjbkE7nqjR+EASnUo94rs/6uNuIDjZeQi1RqzoglNkTi4CzWJKqMkLqL6Q==:raop5Mm1KkbSYLn5fYeqfMqb3KpeQ+D/2yf7cNr80Ms=; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C19771%7CMCMID%7C11869916097808963983367369992461958710%7CMCAAMLH-1696720909%7C9%7CMCAAMB-1708196910%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1708234530s%7CNONE%7CvVersion%7C5.5.0; nlbi_1610353_2147483392=sxL4ZJW+E0Uk4MM06eNT2gAAAABwWICAP3ayLzTmnA3mTT3C; mbox=PC^#ce59f74b0f0d4c0faf786f0cdd04a8f5.35_0^#1771472131|session^#d0039609e0774e019f0edc9dd8cb8227^#1708229191; OptanonConsent=consentId=87bbb087-9363-4ddf-90e1-24e6bc4b7284&datestamp=Sat+Feb+17+2024+19%3A35%3A30+GMT-0800+(Pacific+Standard+Time)&version=202306.2.0&interactionCount=2&isGpcEnabled=0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=US%3BWA',
  'ocp-apim-subscription-key': 'e914eec9448c4d5eb672debf5011cf8f',
  'referer': 'https://www.safeway.com/shop/search-results.html?q=drink',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

roseaursHeader = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'no-cache, no-store',
  'Connection': 'keep-alive',
  'Cookie': '__zlcmid=1KMmVN5TrPnqinJ; inbound_store=817; remember_user_token=BAhbCFsGaQPedrEiIiQyYSQxMCQ4Ym1DOXZCajJXQURIZk44SXZNeHAuSSIWMTcwODE5NDYxNy4wMDg3NjMGOgZFRg%3D%3D--2343f5f83f8bcb2e3032949a2d050d6d7f104236; _rosie_server_session=bENWL3YwRUJrTE5XNU93OFlXN20yVHRDSmZ6d2Y3NDVod1hkUm5vcVZJbi9CN25iY3RQcEMxTmFpdkpJUjF4a1lRdStlT2lnaTMyczIwMDFUS3c1LzduZmVyNnlUazkzWk53MUlSMHZOOEJwM1lhVGYxZUw0SkR6WlRTaUZUNHlJTjBnOGJ4WSt1cFovcjVqTE44Vi9VY0tWRXVwVVg1UWhpRGYxTFFwK2JFaDZ3bENiTW1OZFZFUmpVZnU0VmZuWE9PTWNqWVN2UTdyYmExVVgvZ2hNM0pGZS8rQVlhRTRTbkpOa3pja2dmVUx1THBFOVpFT0NJc1NQMXY1WDRZN1BZNEhUTDh3bkxYNENCbk9sSXhPOVFiS3M4THRUdzF5Y0h5VXNidlY4NkVjTE9NamdwRFZkZkNtc3ZDVG5aSG1xaGJZVStERm52SUFveE1SRHVtSlZTRDF2OC82ZkRnNjI0Q0FWKzFPQVNBPS0tclZ3dmhHczM1bk9JdFZVM3Z4RmVGQT09--3873d8d90eda2a61cfe497953cd04fce8e271255; _rosie_server_session=RlcrNithNU9oNzNuUzdUZWZXT09zR0ZYWXk4c2xOL0Q2OXpqL09OcUJldUxlWkZ3SlkwZXVYTS9FbTIxUjErMmErWmVUM3Nuc3VQTWczM0JkVGtyQ1BXWEkreGdtcFRqUVYyS3VabndtTklPbGJSb2J2WTVSRkFKY3NDWTNrT2NlZ1kvWXJubFVUeUtDbHZBSXdqOU9QemZCWlN2SjlscGkvS3ltYnFORUlpY1lWQ3dJQ25UYjRkUDBSanhOdzUxQnZIVVczbUJ3dzA0TForcTR1YzlkSnM4ZjJwSWdhZDZ1QkFUT2dSLzM2RUZHSklKRC8wL3lCVzBmMEEzSGV3cGFta3U0TUxzNkt4RnAwaURzWUYzUVJvem5HNS8vc3IwSGczWHdoM2hNU29yRUdmVWI3VnhqUmRWM1pzdTBjVmdrQVBOLzdiTUVvZUh1eVg0Rm9CR2VjemhIKzVKM2ZPU2VkaDlqY0pyRUFBPS0tcWN3cUp0OSswUllQRS9rczJsQ3IrQT09--977ff4bf4dff156c3648f0f7c8f9a5c5a368cedb',
  'Referer': 'https://shop.rosieapp.com/rosauers_43/search/milk',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'x-csrf-token': '5NWQlt3zgAiZFDsa4lBMDpAa1CXZpVTo5HqpP0xmyQTJN+4TDkeI5jRLjg6/HVPpHysIMIpKjRocTVqP2XtTtA=='
}
#Returns Website Http Information Object, Takes string
#More info found here: https://www.w3schools.com/python/ref_requests_response.asp
def getWebsiteHttps(keyItem):
    if str.isspace(keyItem):
        return None
    httpOfSearch = []

    url = "https://www.walmart.com/search?q=" + keyItem
    httpOfSearch.append(requests.get(url, headers=walmartHeader).text)

    url = "https://shop.rosieapp.com/v2/user/products?page%5Bnumber%5D=1&page%5Bsize%5D=30&filter%5Bfulltext%5D=" + keyItem
    httpOfSearch.append(requests.get(url, headers = roseaursHeader).text)

    url = "https://www.safeway.com/shop/search-results.html?q=" + keyItem
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    httpOfSearch.append(browser.page_source)
    browser.quit()
    return httpOfSearch
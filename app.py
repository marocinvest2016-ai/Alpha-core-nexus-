elif choice == "💬 المحادثة الذكية مع وكيل تساوت":
    import os

    def load_offers():
        file_path = "descriptions.txt"
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return [line.strip() for line in lines[1:] if "|" in line]

    st.header("💬 المحادثة الذكية مع وكيل تساوت")
    st.write("اسأل عن عقارات قلعة السراغنة...")

    user_input = st.text_input("اكتب سؤالك هنا:", key="chat_input")

    if st.button("إرسال", key="send_chat"):
        if user_input:
            offers = load_offers()
            found = False
            matched_offers = []

            for offer in offers:
                if any(word in offer.lower() for word in user_input.lower().split() if len(word) > 3):
                    matched_offers.append(offer)
                    found = True

            # الروابط ديالك
            youtube = "https://www.youtube.com/@studiotassaout"
            facebook = "https://www.facebook.com/share/1DLCrNYLbV/"
            maps = "https://share.google/M2eVdABaJqJEUqppj"
            whatsapp = "https://wa.me/212691897126"

            if found:
                response = f"""مرحباً بك في وكالة السلام العقارية بقلعة السراغنة 🏢

✅ لقينا عروض قريبة لطلبك:
{matched_offers[0]}

📍 موقعنا: {maps}
📞 للمعاينة: +212 691-897126
💬 واتساب مباشر: {whatsapp}

تابعنا:
▶️ YouTube: {youtube}
📘 Facebook: {facebook}"""
            else:
                response = f"""مرحباً بك في وكالة السلام العقارية بقلعة السراغنة 🏢

طلبك: {user_input}
حاليا ما عندناش هاد العرض بالضبط.

📍 موقعنا: {maps}
📞 تواصل: +212 691-897126
💬 واتساب: {whatsapp}

شوف عروضنا:
▶️ YouTube: {youtube}
📘 Facebook: {facebook}"""

            st.success(response)
            st.link_button("💬 تواصل عبر واتساب الآن", whatsapp, type="primary")

        else:
            st.warning("من فضلك اكتب سؤالك")

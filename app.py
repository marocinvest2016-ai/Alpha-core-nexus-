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

            if found:
                response = f"""مرحباً بك في وكالة السلام العقارية بقلعة السراغنة 🏢

✅ لقينا عروض قريبة لطلبك:
{matched_offers[0]}

📍 الموقع: https://share.google/9QQ0o94SpD3zAnzZh
📞 للمعاينة والحجز: +212 691-897126
قلعة السراغنة - قرب تجزئة العواطف 2"""
            else:
                response = f"""مرحباً بك في وكالة السلام العقارية بقلعة السراغنة 🏢

طلبك: {user_input}
حاليا ما عندناش هاد العرض بالضبط ولكن عندنا عروض أخرى.

📞 تواصل معنا للمزيد: +212 691-897126
📍 الموقع: https://share.google/9QQ0o94SpD3zAnzZh"""

            st.success(response)
        else:
            st.warning("من فضلك اكتب سؤالك")

def write_shopping_list(query):
    with open("shopping_list.txt", "w", encoding="utf8") as file:
        for item in query:
            file.write(
                f"{item.get('ingredient__name')}"
                f"- {item.get('amount__sum')}\n"
            )
    print("Successfuly writed")

ver = "0.17"

ver = "0.3"

class Member:
    def __init__(self, name, words=""):
        self.name = name
        self.words = words

    def name(self):
        return self.name

print("メンバーリスト・アプリ  Ver. "+ver)
print("--------------------------------")

# メンバー追加
mlist = []
newmember = Member("江頭2:50", "エガちゃんです！")
mlist.append(newmember)

### 以下に自分を追加する ###
newmember = Member("小島匠人", "です！")
mlist.append(newmember)

### 以下に自分を追加する ###

newmember = Member("小島 匠人", "です")
mlist.append(newmember)

newmember = Member("大橋 諒太郎", "よろしくお願いします！")
mlist.append(newmember)

newmember = Member("吉田 瑠希也", "よろしくお願いします！")
mlist.append(newmember)

newmember = Member("ハルルルル", "松下です！")
mlist.append(newmember)

newmember = Member("房州優樹", "よろしくです！")
mlist.append(newmember)

newmember = Member("蜂屋 孝太郎", "アタオカです！")
mlist.append(newmember)

newmember = Member("岡 拓未", "よろしくです！")
mlist.append(newmember)

newmember = Member("吉田 羅生", "よろしくです！")
mlist.append(newmember)

newmember = Member("大河原翔太", "よろしくお願いいたします。")
mlist.append(newmember)

newmember = Member("渡邉 雄太", "よろしく！")
mlist.append(newmember)

newmember = Member("樋口　柊", "元気です！")
mlist.append(newmember)

newmember = Member("岸野航", "よろしくです！")
mlist.append(newmember)

newmember = Member("岩崎泰斗", "おなかへりました")
mlist.append(newmember)

newmember = Member("笹谷拓斗", "よろしく")
mlist.append(newmember)

newmember = Member("山口 凜々子", "こんにちは")
mlist.append(newmember)
newmember = Member("玉村　彩", "オーキャン参加します")
mlist.append(newmember)

newmember = Member("小犬丸 愛花", "とても眠いです")
mlist.append(newmember)

# メンバー表示
print("各メンバーから一言")
print()
for member in mlist:
    print(member.name + " ..... " + member.words)

# no_girl_with_you
这个程序是一个社会行为模拟器，模拟女孩选择策略，在n排n列的座位中，女孩们只会选择坐在帅哥身边，女孩不会坐在丑男前后左右四个位置。



这个程序是一个社会行为模拟器，模拟女孩选择策略，在n排n列的座位中，女孩们只会选择坐在帅哥身边，女孩们会尽可能近的靠近帅哥并展现出“😘“，女孩们不会坐在丑男的前后左右四个座椅，如果所有符合条件的座位都满了，你可以点击Checkbox，点击之后，女孩们会坐在丑男旁边，但是会露出“🤮”的表情。

用法：
你可以一次性生成一个女孩，也可以生成自定义数量的女孩。
点击“重新生成“即可重新开始。
丑男/帅哥/座椅排和列均可自定义。

Emoj示例：
女孩：😘
女孩呕吐：🤮
帅哥：😀
丑男：😭
座椅：💺

一些事项：
程序最好运行在win11环境。
如果你发现运行不了:
1.	你是win10系统：
修改”from win11toast import notify”为”from win10toast import notify”；
2.	如果你是其他系统:
删除” from win11toast import notify”;
替换” notify('女孩的消息','座位满了，没位置了！我也不想挨着长得不帅的男孩。看来我只能站着了')”和“notify('系统', '所有座位已坐满')“你喜欢的消息输出模式。

截图:

![1](https://github.com/user-attachments/assets/763a80a1-54a8-4a87-8683-b7418060cc4b)

![2](https://github.com/user-attachments/assets/7a963e74-3624-461b-a02c-fcba5c7b296b)

![3](https://github.com/user-attachments/assets/6c2d992b-cc31-4d85-8e45-7c732d3b383b)

![4](https://github.com/user-attachments/assets/0e9254cb-7dd2-499d-ba87-2ced2f43039d)

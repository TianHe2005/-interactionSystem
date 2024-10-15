import json
import jsonpickle
class VoiceAction:
    def __init__(self, name: str, level: str, type: str, judge: str, keys: str):
        # 动作名称
        self.name = name
        # 优先级
        self.level = level
        # 动作类型 自定义 或者我这边预先设置好的
        self.type = type
        # 动作判断条件
        self.judge = judge
        # 对应的按键招收
        self.keys = keys
        self.actions = []


    def add_action(self, action):
        """添加一个动作到 VoiceAction 实例的动作列表中"""
        self.actions.append(action)

    def get_actions(self):
        """获取 VoiceAction 实例的所有动作"""
        return self.actions


    def to_json(self):
        """将 VoiceAction 实例转换为 JSON 字符串"""
        return jsonpickle.encode(self)


    @classmethod
    def from_json(cls, json_str):
        """从 JSON 字符串创建 VoiceAction 实例"""
        return jsonpickle.decode(json_str)
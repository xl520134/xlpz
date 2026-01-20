from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
# 导入依赖
import aiohttp
import asyncio
import json

@register("helloworld", "YourName", "一个简单的 Hello World 插件（包含随机一言、随机情话、趣味笑话、网易语录、伤感语录功能）", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

#    # 原有 hello world 指令
# #   @filter.command("你好")
# #   async def helloworld(self, event: AstrMessageEvent):
# #       """这是一个 hello world 指令"""
#        user_name = event.get_sender_name()
#        message_str = event.message_str # 用户发的纯文本消息字符串
#        message_chain = event.get_messages() # 用户所发的消息的消息链
#        logger.info(message_chain)
#        yield event.plain_result(f"你好啊!") 

    # 随机一言 指令
    @filter.command("随机一言")
    async def random_word(self, event: AstrMessageEvent):
        """获取一条随机一言"""
        api_url = "https://www.klapi.cn/api/yiyan.php?type="
        
        try:
            # 设置超时时间，避免请求卡住
            timeout = aiohttp.ClientTimeout(total=10)
            
            # 异步请求 API
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(api_url) as response:
                    # 检查响应状态码
                    if response.status == 200:
                        # 读取响应内容（API 返回的是纯文本）
                        result = await response.text()
                        # 去除首尾空白字符
                        result = result.strip()
                        
                        # 如果返回内容不为空，返回给用户
                        if result:
                            yield event.plain_result(result)
                        else:
                            yield event.plain_result("😯 随机一言接口返回空内容了")
                    else:
                        logger.error(f"随机一言API请求失败，状态码：{response.status}")
                        yield event.plain_result(f"❌ 随机一言接口请求失败，状态码：{response.status}")
        
        # 捕获网络相关异常
        except aiohttp.ClientError as e:
            logger.error(f"随机一言API网络请求异常: {str(e)}")
            yield event.plain_result("❌ 网络请求失败，请检查网络或稍后再试")
        
        # 捕获超时异常
        except asyncio.TimeoutError:
            logger.error("随机一言API请求超时")
            yield event.plain_result("⏱️ 请求超时了，请稍后再试")
        
        # 捕获其他未知异常
        except Exception as e:
            logger.error(f"随机一言功能执行异常: {str(e)}")
            yield event.plain_result(f"❌ 发生未知错误：{str(e)}")

    # 随机情话 指令
    @filter.command("随机情话")
    async def random_love(self, event: AstrMessageEvent):
        """获取一条随机情话"""
        api_url = "https://api.tangdouz.com/love.php"
        
        try:
            # 设置超时时间，避免请求卡住
            timeout = aiohttp.ClientTimeout(total=10)
            
            # 异步请求 API
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(api_url) as response:
                    # 检查响应状态码
                    if response.status == 200:
                        # 读取响应内容（API 返回的是纯文本）
                        result = await response.text()
                        # 去除首尾空白字符
                        result = result.strip()
                        
                        # 如果返回内容不为空，返回给用户
                        if result:
                            yield event.plain_result(f"💖 {result}")
                        else:
                            yield event.plain_result("😯 随机情话接口返回空内容了")
                    else:
                        logger.error(f"随机情话API请求失败，状态码：{response.status}")
                        yield event.plain_result(f"❌ 随机情话接口请求失败，状态码：{response.status}")
        
        # 捕获网络相关异常
        except aiohttp.ClientError as e:
            logger.error(f"随机情话API网络请求异常: {str(e)}")
            yield event.plain_result("❌ 网络请求失败，请检查网络或稍后再试")
        
        # 捕获超时异常
        except asyncio.TimeoutError:
            logger.error("随机情话API请求超时")
            yield event.plain_result("⏱️ 请求超时了，请稍后再试")
        
        # 捕获其他未知异常
        except Exception as e:
            logger.error(f"随机情话功能执行异常: {str(e)}")
            yield event.plain_result(f"❌ 发生未知错误：{str(e)}")

    # 趣味笑话 指令
    @filter.command("趣味笑话")
    async def random_joke(self, event: AstrMessageEvent):
        """获取一条趣味笑话"""
        api_url = "https://api.tangdouz.com/xh.php"
        
        try:
            # 设置超时时间，避免请求卡住
            timeout = aiohttp.ClientTimeout(total=10)
            
            # 异步请求 API
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(api_url) as response:
                    # 检查响应状态码
                    if response.status == 200:
                        # 读取响应内容（API 返回的是纯文本）
                        result = await response.text()
                        # 去除首尾空白字符
                        result = result.strip()
                        
                        # 如果返回内容不为空，返回给用户
                        if result:
                            yield event.plain_result(f"😂 {result}")
                        else:
                            yield event.plain_result("😯 趣味笑话接口返回空内容了")
                    else:
                        logger.error(f"趣味笑话API请求失败，状态码：{response.status}")
                        yield event.plain_result(f"❌ 趣味笑话接口请求失败，状态码：{response.status}")
        
        # 捕获网络相关异常
        except aiohttp.ClientError as e:
            logger.error(f"趣味笑话API网络请求异常: {str(e)}")
            yield event.plain_result("❌ 网络请求失败，请检查网络或稍后再试")
        
        # 捕获超时异常
        except asyncio.TimeoutError:
            logger.error("趣味笑话API请求超时")
            yield event.plain_result("⏱️ 请求超时了，请稍后再试")
        
        # 捕获其他未知异常
        except Exception as e:
            logger.error(f"趣味笑话功能执行异常: {str(e)}")
            yield event.plain_result(f"❌ 发生未知错误：{str(e)}")

    # 网易语录 指令
    @filter.command("网易语录")
    async def netease_quote(self, event: AstrMessageEvent):
        """获取一条网易云热评语录"""
        api_url = "https://v1.hitokoto.cn/"
        
        try:
            # 设置超时时间，避免请求卡住
            timeout = aiohttp.ClientTimeout(total=10)
            
            # 异步请求 API
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(api_url) as response:
                    # 检查响应状态码
                    if response.status == 200:
                        # 读取并解析JSON响应内容
                        result = await response.json()
                        
                        # 提取hitokoto字段值
                        quote_content = result.get("hitokoto")
                        if quote_content and quote_content.strip():
                            yield event.plain_result(f"📝 {quote_content.strip()}")
                        else:
                            yield event.plain_result("😯 网易语录接口返回空内容了")
                    else:
                        logger.error(f"网易语录API请求失败，状态码：{response.status}")
                        yield event.plain_result(f"❌ 网易语录接口请求失败，状态码：{response.status}")
        
        # 捕获JSON解析异常
        except json.JSONDecodeError as e:
            logger.error(f"网易语录API返回的JSON格式错误: {str(e)}")
            yield event.plain_result("❌ 接口返回数据格式错误，无法解析语录内容")
        
        # 捕获网络相关异常
        except aiohttp.ClientError as e:
            logger.error(f"网易语录API网络请求异常: {str(e)}")
            yield event.plain_result("❌ 网络请求失败，请检查网络或稍后再试")
        
        # 捕获超时异常
        except asyncio.TimeoutError:
            logger.error("网易语录API请求超时")
            yield event.plain_result("⏱️ 请求超时了，请稍后再试")
        
        # 捕获其他未知异常
        except Exception as e:
            logger.error(f"网易语录功能执行异常: {str(e)}")
            yield event.plain_result(f"❌ 发生未知错误：{str(e)}")

    # 新增 伤感语录 指令
    @filter.command("伤感语录")
    async def sad_quote(self, event: AstrMessageEvent):
        """获取一条伤感语录"""
        api_url = "https://api.yuafeng.cn/API/ly/shanggan.php?type=text"
        
        try:
            # 设置超时时间，避免请求卡住
            timeout = aiohttp.ClientTimeout(total=10)
            
            # 异步请求 API
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(api_url) as response:
                    # 检查响应状态码
                    if response.status == 200:
                        # 读取响应内容（API 返回的是纯文本）
                        result = await response.text()
                        # 去除首尾空白字符
                        result = result.strip()
                        
                        # 如果返回内容不为空，返回给用户
                        if result:
                            yield event.plain_result(f"💔 {result}")  # 心碎emoji贴合伤感主题
                        else:
                            yield event.plain_result("😯 伤感语录接口返回空内容了")
                    else:
                        logger.error(f"伤感语录API请求失败，状态码：{response.status}")
                        yield event.plain_result(f"❌ 伤感语录接口请求失败，状态码：{response.status}")
        
        # 捕获网络相关异常
        except aiohttp.ClientError as e:
            logger.error(f"伤感语录API网络请求异常: {str(e)}")
            yield event.plain_result("❌ 网络请求失败，请检查网络或稍后再试")
        
        # 捕获超时异常
        except asyncio.TimeoutError:
            logger.error("伤感语录API请求超时")
            yield event.plain_result("⏱️ 请求超时了，请稍后再试")
        
        # 捕获其他未知异常
        except Exception as e:
            logger.error(f"伤感语录功能执行异常: {str(e)}")
            yield event.plain_result(f"❌ 发生未知错误：{str(e)}")

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
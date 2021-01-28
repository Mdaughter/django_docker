# coding=utf-8
from django.contrib import admin
from django.core.cache import cache
from goods.models import GoodsType, IndexPromotionBanner, IndexGoodsBanner,  IndexTypeGoodsBanner, GoodsSKU, Goods
from django.template import loader
from django.conf import settings
import os
from asgiref.sync import sync_to_async
# Register your models here.


def generate_static_index_html():
    """使用celery生成静态首页文件"""
    # 获取商品的分类信息
    types = GoodsType.objects.all()

    # 获取首页的轮播商品的信息
    index_banner = IndexGoodsBanner.objects.all().order_by('index')

    # 获取首页的促销活动的信息
    promotion_banner = IndexPromotionBanner.objects.all().order_by('index')

    # 获取首页分类商品的展示信息
    for category in types:
        # 获取type种类在首页展示的图片商品的信息和文字商品的信息
        image_banner = IndexTypeGoodsBanner.objects.filter(category=category, display_type=1)
        title_banner = IndexTypeGoodsBanner.objects.filter(category=category, display_type=0)

        # 给category对象增加属性title_banner,image_banner
        # 分别保存category种类在首页展示的文字商品和图片商品的信息
        category.title_banner = title_banner
        category.image_banner = image_banner

    cart_count = 0

    # 组织模板上下文
    context = {
        'types': types,
        'index_banner': index_banner,
        'promotion_banner': promotion_banner,
        'cart_count': cart_count,
    }

    # 使用模板

    # 1.加载模板文件
    temp = loader.get_template('goods/static_index.html')
    # 2.模板渲染
    static_html = temp.render(context)
    # 3.生成静态首页文件
    save_path = os.path.join(settings.BASE_DIR, 'static_new/www/index.html')
    with open(save_path, 'w') as f:
        f.write(static_html)

class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """新增或更新时调用"""
        # 调用ModelAdmin中save_model来实现更新或新增
        super().save_model(request, obj, form, change)

        # 附加操作：发出生成静态首页的任务
        print('发出重新生成静态首页的任务')
        sync_to_async(generate_static_index_html(), thread_sensitive=True)
        # 附加操作: 清除首页缓存
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        """删除数据时调用"""
        # 调用ModelAdmin中delete_model来实现删除操作
        super().delete_model(request, obj)

        # 附加操作：发出生成静态首页的任
        print('发出重新生成静态首页的任务')
        sync_to_async(generate_static_index_html(), thread_sensitive=True)
        # 附加操作: 清除首页缓存
        cache.delete('index_page_data')


class GoodsTypeAdmin(BaseModelAdmin):
    """商品种类模型admin管理类"""
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    """首页轮播商品模型admin管理类"""
    pass


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    """首页分类商品展示模型admi管理类"""
    pass


class IndexPromotionBannerAdmin(BaseModelAdmin):
    """首页促销活动admin管理类"""
    pass


class GoodsSKUAdmin(BaseModelAdmin):
    """首页促销活动admin管理类"""
    pass


class GoodsAdmin(BaseModelAdmin):
    """首页促销活动admin管理类"""
    pass


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
admin.site.register(GoodsSKU, GoodsSKUAdmin)
admin.site.register(Goods, GoodsAdmin)

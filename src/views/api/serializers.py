from cms.models.pagemodel import Page
from easy_thumbnails.files import get_thumbnailer
from rest_framework import serializers
from cms.plugin_rendering import ContentRenderer



class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    absolute_url = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['title', 'absolute_url', 'image', 'body', 'publication_date']

    def get_title(self, obj):
        """
        Returns the title of the CMS page.
        """
        return obj.get_title()

    def get_absolute_url(self, obj):
        """
        Returns the absolute url of the CMS page.
        """
        return obj.get_absolute_url()

    def get_image(self, obj):
        """
        Returns the (thumbnailer processed) image for this CMS page.
        """
        options = { 'size': (768, 288), 'crop': True, 'upscale': True, 'subject_location': obj.articleextension.image.subject_location }
        return get_thumbnailer(obj.articleextension.image).get_thumbnail(options).url

    def get_body(self, obj):
        """
        Returns the output of all the plugins of this CMS page.
        """
        body = ''
        context = self.context
        context['cms_content_renderer'] = ContentRenderer(self.context['request'])

        for placeholder in obj.get_placeholders():
            for plugin in placeholder.get_plugins():
                body += plugin.render_plugin(context)
        return body

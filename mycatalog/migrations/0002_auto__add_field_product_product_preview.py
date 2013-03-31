# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.product_preview'
        db.add_column(u'mycatalog_product', 'product_preview',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.product_preview'
        db.delete_column(u'mycatalog_product', 'product_preview')


    models = {
        u'mycatalog.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_color': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_description': ('django.db.models.fields.TextField', [], {}),
            'product_height': ('django.db.models.fields.IntegerField', [], {}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product_weight': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['mycatalog']
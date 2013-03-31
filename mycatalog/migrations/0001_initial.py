# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'mycatalog_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product_description', self.gf('django.db.models.fields.TextField')()),
            ('product_weight', self.gf('django.db.models.fields.IntegerField')()),
            ('product_height', self.gf('django.db.models.fields.IntegerField')()),
            ('product_color', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'mycatalog', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'mycatalog_product')


    models = {
        u'mycatalog.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_color': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_description': ('django.db.models.fields.TextField', [], {}),
            'product_height': ('django.db.models.fields.IntegerField', [], {}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_weight': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['mycatalog']
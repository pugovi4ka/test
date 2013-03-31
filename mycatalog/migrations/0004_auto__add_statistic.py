# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Statistic'
        db.create_table(u'mycatalog_statistic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('response_status_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'mycatalog', ['Statistic'])


    def backwards(self, orm):
        # Deleting model 'Statistic'
        db.delete_table(u'mycatalog_statistic')


    models = {
        u'mycatalog.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_color': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_color_once_more': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_description': ('django.db.models.fields.TextField', [], {}),
            'product_height': ('django.db.models.fields.IntegerField', [], {}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product_weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mycatalog.statistic': {
            'Meta': {'object_name': 'Statistic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'response_status_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mycatalog']
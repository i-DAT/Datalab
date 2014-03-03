# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Motion'
        db.create_table(u'perception_motion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('camera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perception.Camera'])),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'perception', ['Motion'])


    def backwards(self, orm):
        # Deleting model 'Motion'
        db.delete_table(u'perception_motion')


    models = {
        u'perception.camera': {
            'Meta': {'object_name': 'Camera'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'perception.motion': {
            'Meta': {'object_name': 'Motion'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'camera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perception.Camera']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        u'perception.volume': {
            'Meta': {'object_name': 'Volume'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'camera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['perception.Camera']"}),
            'decibels': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['perception']
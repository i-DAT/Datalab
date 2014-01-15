# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Install'
        db.create_table(u'mapping_install', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mapping', ['Install'])

        # Adding model 'Imp'
        db.create_table(u'mapping_imp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('install', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapping.Install'])),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('long', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mapping', ['Imp'])

        # Adding model 'Sensor'
        db.create_table(u'mapping_sensor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('scale', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mapping', ['Sensor'])

        # Adding model 'Reading'
        db.create_table(u'mapping_reading', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapping.Imp'])),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapping.Sensor'])),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'mapping', ['Reading'])

        # Adding model 'Device'
        db.create_table(u'mapping_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mapping', ['Device'])

        # Adding model 'Location'
        db.create_table(u'mapping_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapping.Device'])),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('long', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('activity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('confidence', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'mapping', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Install'
        db.delete_table(u'mapping_install')

        # Deleting model 'Imp'
        db.delete_table(u'mapping_imp')

        # Deleting model 'Sensor'
        db.delete_table(u'mapping_sensor')

        # Deleting model 'Reading'
        db.delete_table(u'mapping_reading')

        # Deleting model 'Device'
        db.delete_table(u'mapping_device')

        # Deleting model 'Location'
        db.delete_table(u'mapping_location')


    models = {
        u'mapping.device': {
            'Meta': {'object_name': 'Device'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'mapping.imp': {
            'Meta': {'object_name': 'Imp'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapping.Install']"}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'mapping.install': {
            'Meta': {'object_name': 'Install'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'mapping.location': {
            'Meta': {'object_name': 'Location'},
            'activity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'confidence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapping.Device']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'})
        },
        u'mapping.reading': {
            'Meta': {'object_name': 'Reading'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'amount': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapping.Imp']"}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapping.Sensor']"})
        },
        u'mapping.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'scale': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mapping']
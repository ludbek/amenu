# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GenericMenuModel'
        db.create_table(u'amenu_genericmenumodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('start_level', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('end_level', self.gf('django.db.models.fields.PositiveIntegerField')(default=100)),
            ('extra_inactive', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('extra_active', self.gf('django.db.models.fields.PositiveIntegerField')(default=100)),
        ))
        db.send_create_signal(u'amenu', ['GenericMenuModel'])


    def backwards(self, orm):
        # Deleting model 'GenericMenuModel'
        db.delete_table(u'amenu_genericmenumodel')


    models = {
        u'amenu.breadcrumbmodel': {
            'Meta': {'object_name': 'BreadcrumbModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'start_level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'amenu.genericmenumodel': {
            'Meta': {'object_name': 'GenericMenuModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'end_level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100'}),
            'extra_active': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100'}),
            'extra_inactive': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'start_level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'amenu.menubelowthismodel': {
            'Meta': {'object_name': 'MenuBelowThisModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '3'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['amenu']
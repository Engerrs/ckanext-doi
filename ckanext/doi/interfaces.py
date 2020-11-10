#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-doi
# Created by the Natural History Museum in London, UK

from ckan.plugins import interfaces


class IDoi(interfaces.Interface):
    '''Hook into IDoi'''

    def build_metadata_dict(self, pkg_dict, metadata_dict, errors):
        '''Extracts metadata from a pkg_dict for use in generating datacite DOIs. Extends the
        build_metadata_dict method from ckanext-doi.

        :param pkg_dict: package dictionary
        :param metadata_dict: the current metadata dict, created by the ckanext-doi extension and
                              any previous plugins implementing IDoi
        :param errors: a dictionary of metadata keys and errors generated by previous plugins;
                       this method should remove any keys that it successfully processes and
                       overwrites
        :returns: metadata_dict, errors
        '''
        return metadata_dict, errors

    def build_xml_dict(self, metadata_dict, xml_dict):
        '''Converts the metadata_dict into an xml_dict that can be passed to the datacite
        library's schema42.tostring() and schema42.validate() methods. Extends the
        build_xml_dict() method from ckanext-doi.

        :param metadata_dict: the metadata dict generated from build_metadata_dict
        :param xml_dict: XML dict to pass to schema42.validate()
        :returns: xml_dict
        '''
        return xml_dict

    def is_updated(self, pkg_dict):
        return False

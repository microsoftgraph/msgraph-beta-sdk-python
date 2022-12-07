from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_definition = lazy_import('msgraph.generated.models.group_policy_definition')
group_policy_type = lazy_import('msgraph.generated.models.group_policy_type')

class GroupPolicyDefinitionFile(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyDefinitionFile and sets the default values.
        """
        super().__init__()
        # The group policy definitions associated with the file.
        self._definitions: Optional[List[group_policy_definition.GroupPolicyDefinition]] = None
        # The localized description of the policy settings in the ADMX file. The default value is empty.
        self._description: Optional[str] = None
        # The localized friendly name of the ADMX file.
        self._display_name: Optional[str] = None
        # The file name of the ADMX file without the path. For example: edge.admx
        self._file_name: Optional[str] = None
        # The supported language codes for the ADMX file.
        self._language_codes: Optional[List[str]] = None
        # The date and time the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Type of Group Policy File or Definition.
        self._policy_type: Optional[group_policy_type.GroupPolicyType] = None
        # The revision version associated with the file.
        self._revision: Optional[str] = None
        # Specifies the URI used to identify the namespace within the ADMX file.
        self._target_namespace: Optional[str] = None
        # Specifies the logical name that refers to the namespace within the ADMX file.
        self._target_prefix: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyDefinitionFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyDefinitionFile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyDefinitionFile()
    
    @property
    def definitions(self,) -> Optional[List[group_policy_definition.GroupPolicyDefinition]]:
        """
        Gets the definitions property value. The group policy definitions associated with the file.
        Returns: Optional[List[group_policy_definition.GroupPolicyDefinition]]
        """
        return self._definitions
    
    @definitions.setter
    def definitions(self,value: Optional[List[group_policy_definition.GroupPolicyDefinition]] = None) -> None:
        """
        Sets the definitions property value. The group policy definitions associated with the file.
        Args:
            value: Value to set for the definitions property.
        """
        self._definitions = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The localized description of the policy settings in the ADMX file. The default value is empty.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The localized description of the policy settings in the ADMX file. The default value is empty.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The localized friendly name of the ADMX file.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The localized friendly name of the ADMX file.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. The file name of the ADMX file without the path. For example: edge.admx
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. The file name of the ADMX file without the path. For example: edge.admx
        Args:
            value: Value to set for the fileName property.
        """
        self._file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(group_policy_definition.GroupPolicyDefinition)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "language_codes": lambda n : setattr(self, 'language_codes', n.get_collection_of_primitive_values(str)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "policy_type": lambda n : setattr(self, 'policy_type', n.get_enum_value(group_policy_type.GroupPolicyType)),
            "revision": lambda n : setattr(self, 'revision', n.get_str_value()),
            "target_namespace": lambda n : setattr(self, 'target_namespace', n.get_str_value()),
            "target_prefix": lambda n : setattr(self, 'target_prefix', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def language_codes(self,) -> Optional[List[str]]:
        """
        Gets the languageCodes property value. The supported language codes for the ADMX file.
        Returns: Optional[List[str]]
        """
        return self._language_codes
    
    @language_codes.setter
    def language_codes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the languageCodes property value. The supported language codes for the ADMX file.
        Args:
            value: Value to set for the languageCodes property.
        """
        self._language_codes = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def policy_type(self,) -> Optional[group_policy_type.GroupPolicyType]:
        """
        Gets the policyType property value. Type of Group Policy File or Definition.
        Returns: Optional[group_policy_type.GroupPolicyType]
        """
        return self._policy_type
    
    @policy_type.setter
    def policy_type(self,value: Optional[group_policy_type.GroupPolicyType] = None) -> None:
        """
        Sets the policyType property value. Type of Group Policy File or Definition.
        Args:
            value: Value to set for the policyType property.
        """
        self._policy_type = value
    
    @property
    def revision(self,) -> Optional[str]:
        """
        Gets the revision property value. The revision version associated with the file.
        Returns: Optional[str]
        """
        return self._revision
    
    @revision.setter
    def revision(self,value: Optional[str] = None) -> None:
        """
        Sets the revision property value. The revision version associated with the file.
        Args:
            value: Value to set for the revision property.
        """
        self._revision = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("definitions", self.definitions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("fileName", self.file_name)
        writer.write_collection_of_primitive_values("languageCodes", self.language_codes)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("policyType", self.policy_type)
        writer.write_str_value("revision", self.revision)
        writer.write_str_value("targetNamespace", self.target_namespace)
        writer.write_str_value("targetPrefix", self.target_prefix)
    
    @property
    def target_namespace(self,) -> Optional[str]:
        """
        Gets the targetNamespace property value. Specifies the URI used to identify the namespace within the ADMX file.
        Returns: Optional[str]
        """
        return self._target_namespace
    
    @target_namespace.setter
    def target_namespace(self,value: Optional[str] = None) -> None:
        """
        Sets the targetNamespace property value. Specifies the URI used to identify the namespace within the ADMX file.
        Args:
            value: Value to set for the targetNamespace property.
        """
        self._target_namespace = value
    
    @property
    def target_prefix(self,) -> Optional[str]:
        """
        Gets the targetPrefix property value. Specifies the logical name that refers to the namespace within the ADMX file.
        Returns: Optional[str]
        """
        return self._target_prefix
    
    @target_prefix.setter
    def target_prefix(self,value: Optional[str] = None) -> None:
        """
        Sets the targetPrefix property value. Specifies the logical name that refers to the namespace within the ADMX file.
        Args:
            value: Value to set for the targetPrefix property.
        """
        self._target_prefix = value
    


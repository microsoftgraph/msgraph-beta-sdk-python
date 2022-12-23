from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

allowed_value = lazy_import('msgraph.generated.models.allowed_value')
entity = lazy_import('msgraph.generated.models.entity')

class CustomSecurityAttributeDefinition(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def allowed_values(self,) -> Optional[List[allowed_value.AllowedValue]]:
        """
        Gets the allowedValues property value. Values that are predefined for this custom security attribute.This navigation property is not returned by default and must be specified in an $expand query. For example, /directory/customSecurityAttributeDefinitions?$expand=allowedValues.
        Returns: Optional[List[allowed_value.AllowedValue]]
        """
        return self._allowed_values
    
    @allowed_values.setter
    def allowed_values(self,value: Optional[List[allowed_value.AllowedValue]] = None) -> None:
        """
        Sets the allowedValues property value. Values that are predefined for this custom security attribute.This navigation property is not returned by default and must be specified in an $expand query. For example, /directory/customSecurityAttributeDefinitions?$expand=allowedValues.
        Args:
            value: Value to set for the allowedValues property.
        """
        self._allowed_values = value
    
    @property
    def attribute_set(self,) -> Optional[str]:
        """
        Gets the attributeSet property value. Name of the attribute set. Case insensitive.
        Returns: Optional[str]
        """
        return self._attribute_set
    
    @attribute_set.setter
    def attribute_set(self,value: Optional[str] = None) -> None:
        """
        Sets the attributeSet property value. Name of the attribute set. Case insensitive.
        Args:
            value: Value to set for the attributeSet property.
        """
        self._attribute_set = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new customSecurityAttributeDefinition and sets the default values.
        """
        super().__init__()
        # Values that are predefined for this custom security attribute.This navigation property is not returned by default and must be specified in an $expand query. For example, /directory/customSecurityAttributeDefinitions?$expand=allowedValues.
        self._allowed_values: Optional[List[allowed_value.AllowedValue]] = None
        # Name of the attribute set. Case insensitive.
        self._attribute_set: Optional[str] = None
        # Description of the custom security attribute. Can be up to 128 characters long and include Unicode characters. Can be changed later.
        self._description: Optional[str] = None
        # Indicates whether multiple values can be assigned to the custom security attribute. Cannot be changed later. If type is set to Boolean, isCollection cannot be set to true.
        self._is_collection: Optional[bool] = None
        # Indicates whether custom security attribute values will be indexed for searching on objects that are assigned attribute values. Cannot be changed later.
        self._is_searchable: Optional[bool] = None
        # Name of the custom security attribute. Must be unique within an attribute set. Can be up to 32 characters long and include Unicode characters. Cannot contain spaces or special characters. Cannot be changed later. Case insensitive.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies whether the custom security attribute is active or deactivated. Acceptable values are Available and Deprecated. Can be changed later.
        self._status: Optional[str] = None
        # Data type for the custom security attribute values. Supported types are Boolean, Integer, and String. Cannot be changed later.
        self._type: Optional[str] = None
        # Indicates whether only predefined values can be assigned to the custom security attribute. If set to false, free-form values are allowed. Can later be changed from true to false, but cannot be changed from false to true. If type is set to Boolean, usePreDefinedValuesOnly cannot be set to true.
        self._use_pre_defined_values_only: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomSecurityAttributeDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomSecurityAttributeDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomSecurityAttributeDefinition()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the custom security attribute. Can be up to 128 characters long and include Unicode characters. Can be changed later.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the custom security attribute. Can be up to 128 characters long and include Unicode characters. Can be changed later.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_values": lambda n : setattr(self, 'allowed_values', n.get_collection_of_object_values(allowed_value.AllowedValue)),
            "attribute_set": lambda n : setattr(self, 'attribute_set', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "is_collection": lambda n : setattr(self, 'is_collection', n.get_bool_value()),
            "is_searchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "use_pre_defined_values_only": lambda n : setattr(self, 'use_pre_defined_values_only', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_collection(self,) -> Optional[bool]:
        """
        Gets the isCollection property value. Indicates whether multiple values can be assigned to the custom security attribute. Cannot be changed later. If type is set to Boolean, isCollection cannot be set to true.
        Returns: Optional[bool]
        """
        return self._is_collection
    
    @is_collection.setter
    def is_collection(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCollection property value. Indicates whether multiple values can be assigned to the custom security attribute. Cannot be changed later. If type is set to Boolean, isCollection cannot be set to true.
        Args:
            value: Value to set for the isCollection property.
        """
        self._is_collection = value
    
    @property
    def is_searchable(self,) -> Optional[bool]:
        """
        Gets the isSearchable property value. Indicates whether custom security attribute values will be indexed for searching on objects that are assigned attribute values. Cannot be changed later.
        Returns: Optional[bool]
        """
        return self._is_searchable
    
    @is_searchable.setter
    def is_searchable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSearchable property value. Indicates whether custom security attribute values will be indexed for searching on objects that are assigned attribute values. Cannot be changed later.
        Args:
            value: Value to set for the isSearchable property.
        """
        self._is_searchable = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the custom security attribute. Must be unique within an attribute set. Can be up to 32 characters long and include Unicode characters. Cannot contain spaces or special characters. Cannot be changed later. Case insensitive.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the custom security attribute. Must be unique within an attribute set. Can be up to 32 characters long and include Unicode characters. Cannot contain spaces or special characters. Cannot be changed later. Case insensitive.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("allowedValues", self.allowed_values)
        writer.write_str_value("attributeSet", self.attribute_set)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("isCollection", self.is_collection)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_str_value("name", self.name)
        writer.write_str_value("status", self.status)
        writer.write_str_value("type", self.type)
        writer.write_bool_value("usePreDefinedValuesOnly", self.use_pre_defined_values_only)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. Specifies whether the custom security attribute is active or deactivated. Acceptable values are Available and Deprecated. Can be changed later.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. Specifies whether the custom security attribute is active or deactivated. Acceptable values are Available and Deprecated. Can be changed later.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Data type for the custom security attribute values. Supported types are Boolean, Integer, and String. Cannot be changed later.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Data type for the custom security attribute values. Supported types are Boolean, Integer, and String. Cannot be changed later.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def use_pre_defined_values_only(self,) -> Optional[bool]:
        """
        Gets the usePreDefinedValuesOnly property value. Indicates whether only predefined values can be assigned to the custom security attribute. If set to false, free-form values are allowed. Can later be changed from true to false, but cannot be changed from false to true. If type is set to Boolean, usePreDefinedValuesOnly cannot be set to true.
        Returns: Optional[bool]
        """
        return self._use_pre_defined_values_only
    
    @use_pre_defined_values_only.setter
    def use_pre_defined_values_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the usePreDefinedValuesOnly property value. Indicates whether only predefined values can be assigned to the custom security attribute. If set to false, free-form values are allowed. Can later be changed from true to false, but cannot be changed from false to true. If type is set to Boolean, usePreDefinedValuesOnly cannot be set to true.
        Args:
            value: Value to set for the usePreDefinedValuesOnly property.
        """
        self._use_pre_defined_values_only = value
    


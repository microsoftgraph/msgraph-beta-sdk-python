from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_resource_attribute_destination = lazy_import('msgraph.generated.models.access_package_resource_attribute_destination')
access_package_resource_attribute_source = lazy_import('msgraph.generated.models.access_package_resource_attribute_source')

class AccessPackageResourceAttribute(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def attribute_destination(self,) -> Optional[access_package_resource_attribute_destination.AccessPackageResourceAttributeDestination]:
        """
        Gets the attributeDestination property value. Information about how to set the attribute, currently a accessPackageUserDirectoryAttributeStore object type.
        Returns: Optional[access_package_resource_attribute_destination.AccessPackageResourceAttributeDestination]
        """
        return self._attribute_destination
    
    @attribute_destination.setter
    def attribute_destination(self,value: Optional[access_package_resource_attribute_destination.AccessPackageResourceAttributeDestination] = None) -> None:
        """
        Sets the attributeDestination property value. Information about how to set the attribute, currently a accessPackageUserDirectoryAttributeStore object type.
        Args:
            value: Value to set for the attributeDestination property.
        """
        self._attribute_destination = value
    
    @property
    def attribute_name(self,) -> Optional[str]:
        """
        Gets the attributeName property value. The name of the attribute in the end system. If the destination is accessPackageUserDirectoryAttributeStore, then a user property such as jobTitle or a directory schema extension for the user object type, such as extension_2b676109c7c74ae2b41549205f1947ed_personalTitle.
        Returns: Optional[str]
        """
        return self._attribute_name
    
    @attribute_name.setter
    def attribute_name(self,value: Optional[str] = None) -> None:
        """
        Sets the attributeName property value. The name of the attribute in the end system. If the destination is accessPackageUserDirectoryAttributeStore, then a user property such as jobTitle or a directory schema extension for the user object type, such as extension_2b676109c7c74ae2b41549205f1947ed_personalTitle.
        Args:
            value: Value to set for the attributeName property.
        """
        self._attribute_name = value
    
    @property
    def attribute_source(self,) -> Optional[access_package_resource_attribute_source.AccessPackageResourceAttributeSource]:
        """
        Gets the attributeSource property value. Information about how to populate the attribute value when an accessPackageAssignmentRequest is being fulfilled, currently a accessPackageResourceAttributeQuestion object type.
        Returns: Optional[access_package_resource_attribute_source.AccessPackageResourceAttributeSource]
        """
        return self._attribute_source
    
    @attribute_source.setter
    def attribute_source(self,value: Optional[access_package_resource_attribute_source.AccessPackageResourceAttributeSource] = None) -> None:
        """
        Sets the attributeSource property value. Information about how to populate the attribute value when an accessPackageAssignmentRequest is being fulfilled, currently a accessPackageResourceAttributeQuestion object type.
        Args:
            value: Value to set for the attributeSource property.
        """
        self._attribute_source = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageResourceAttribute and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Information about how to set the attribute, currently a accessPackageUserDirectoryAttributeStore object type.
        self._attribute_destination: Optional[access_package_resource_attribute_destination.AccessPackageResourceAttributeDestination] = None
        # The name of the attribute in the end system. If the destination is accessPackageUserDirectoryAttributeStore, then a user property such as jobTitle or a directory schema extension for the user object type, such as extension_2b676109c7c74ae2b41549205f1947ed_personalTitle.
        self._attribute_name: Optional[str] = None
        # Information about how to populate the attribute value when an accessPackageAssignmentRequest is being fulfilled, currently a accessPackageResourceAttributeQuestion object type.
        self._attribute_source: Optional[access_package_resource_attribute_source.AccessPackageResourceAttributeSource] = None
        # Unique identifier for the attribute on the access package resource. Read-only.
        self._id: Optional[str] = None
        # Specifies whether or not an existing attribute value can be edited by the requester.
        self._is_editable: Optional[bool] = None
        # Specifies whether the attribute will remain in the end system after an assignment ends.
        self._is_persisted_on_assignment_removal: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceAttribute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceAttribute
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageResourceAttribute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attribute_destination": lambda n : setattr(self, 'attribute_destination', n.get_object_value(access_package_resource_attribute_destination.AccessPackageResourceAttributeDestination)),
            "attribute_name": lambda n : setattr(self, 'attribute_name', n.get_str_value()),
            "attribute_source": lambda n : setattr(self, 'attribute_source', n.get_object_value(access_package_resource_attribute_source.AccessPackageResourceAttributeSource)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "is_editable": lambda n : setattr(self, 'is_editable', n.get_bool_value()),
            "is_persisted_on_assignment_removal": lambda n : setattr(self, 'is_persisted_on_assignment_removal', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Unique identifier for the attribute on the access package resource. Read-only.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Unique identifier for the attribute on the access package resource. Read-only.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def is_editable(self,) -> Optional[bool]:
        """
        Gets the isEditable property value. Specifies whether or not an existing attribute value can be edited by the requester.
        Returns: Optional[bool]
        """
        return self._is_editable
    
    @is_editable.setter
    def is_editable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEditable property value. Specifies whether or not an existing attribute value can be edited by the requester.
        Args:
            value: Value to set for the isEditable property.
        """
        self._is_editable = value
    
    @property
    def is_persisted_on_assignment_removal(self,) -> Optional[bool]:
        """
        Gets the isPersistedOnAssignmentRemoval property value. Specifies whether the attribute will remain in the end system after an assignment ends.
        Returns: Optional[bool]
        """
        return self._is_persisted_on_assignment_removal
    
    @is_persisted_on_assignment_removal.setter
    def is_persisted_on_assignment_removal(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPersistedOnAssignmentRemoval property value. Specifies whether the attribute will remain in the end system after an assignment ends.
        Args:
            value: Value to set for the isPersistedOnAssignmentRemoval property.
        """
        self._is_persisted_on_assignment_removal = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("attributeDestination", self.attribute_destination)
        writer.write_str_value("attributeName", self.attribute_name)
        writer.write_object_value("attributeSource", self.attribute_source)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isEditable", self.is_editable)
        writer.write_bool_value("isPersistedOnAssignmentRemoval", self.is_persisted_on_assignment_removal)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_audit_property = lazy_import('msgraph.generated.models.cloud_pc_audit_property')

class CloudPcAuditResource(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcAuditResource and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The resource entity display name.
        self._display_name: Optional[str] = None
        # A list of modified properties.
        self._modified_properties: Optional[List[cloud_pc_audit_property.CloudPcAuditProperty]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The ID of the audit resource.
        self._resource_id: Optional[str] = None
        # The type of the audit resource.
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcAuditResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAuditResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcAuditResource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The resource entity display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The resource entity display name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "modified_properties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(cloud_pc_audit_property.CloudPcAuditProperty)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        return fields
    
    @property
    def modified_properties(self,) -> Optional[List[cloud_pc_audit_property.CloudPcAuditProperty]]:
        """
        Gets the modifiedProperties property value. A list of modified properties.
        Returns: Optional[List[cloud_pc_audit_property.CloudPcAuditProperty]]
        """
        return self._modified_properties
    
    @modified_properties.setter
    def modified_properties(self,value: Optional[List[cloud_pc_audit_property.CloudPcAuditProperty]] = None) -> None:
        """
        Sets the modifiedProperties property value. A list of modified properties.
        Args:
            value: Value to set for the modifiedProperties property.
        """
        self._modified_properties = value
    
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
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. The ID of the audit resource.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. The ID of the audit resource.
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("modifiedProperties", self.modified_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type of the audit resource.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type of the audit resource.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    


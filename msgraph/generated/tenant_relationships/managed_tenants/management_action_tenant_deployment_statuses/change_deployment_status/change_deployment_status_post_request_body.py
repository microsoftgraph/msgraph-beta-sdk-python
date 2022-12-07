from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ChangeDeploymentStatusPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the changeDeploymentStatus method.
    """
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
        Instantiates a new changeDeploymentStatusPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The managementActionId property
        self._management_action_id: Optional[str] = None
        # The managementTemplateId property
        self._management_template_id: Optional[str] = None
        # The managementTemplateVersion property
        self._management_template_version: Optional[int] = None
        # The status property
        self._status: Optional[str] = None
        # The tenantGroupId property
        self._tenant_group_id: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChangeDeploymentStatusPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChangeDeploymentStatusPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChangeDeploymentStatusPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "management_action_id": lambda n : setattr(self, 'management_action_id', n.get_str_value()),
            "management_template_id": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "management_template_version": lambda n : setattr(self, 'management_template_version', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "tenant_group_id": lambda n : setattr(self, 'tenant_group_id', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        return fields
    
    @property
    def management_action_id(self,) -> Optional[str]:
        """
        Gets the managementActionId property value. The managementActionId property
        Returns: Optional[str]
        """
        return self._management_action_id
    
    @management_action_id.setter
    def management_action_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementActionId property value. The managementActionId property
        Args:
            value: Value to set for the managementActionId property.
        """
        self._management_action_id = value
    
    @property
    def management_template_id(self,) -> Optional[str]:
        """
        Gets the managementTemplateId property value. The managementTemplateId property
        Returns: Optional[str]
        """
        return self._management_template_id
    
    @management_template_id.setter
    def management_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateId property value. The managementTemplateId property
        Args:
            value: Value to set for the managementTemplateId property.
        """
        self._management_template_id = value
    
    @property
    def management_template_version(self,) -> Optional[int]:
        """
        Gets the managementTemplateVersion property value. The managementTemplateVersion property
        Returns: Optional[int]
        """
        return self._management_template_version
    
    @management_template_version.setter
    def management_template_version(self,value: Optional[int] = None) -> None:
        """
        Sets the managementTemplateVersion property value. The managementTemplateVersion property
        Args:
            value: Value to set for the managementTemplateVersion property.
        """
        self._management_template_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("managementActionId", self.management_action_id)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_int_value("managementTemplateVersion", self.management_template_version)
        writer.write_str_value("status", self.status)
        writer.write_str_value("tenantGroupId", self.tenant_group_id)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status property
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def tenant_group_id(self,) -> Optional[str]:
        """
        Gets the tenantGroupId property value. The tenantGroupId property
        Returns: Optional[str]
        """
        return self._tenant_group_id
    
    @tenant_group_id.setter
    def tenant_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantGroupId property value. The tenantGroupId property
        Args:
            value: Value to set for the tenantGroupId property.
        """
        self._tenant_group_id = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    


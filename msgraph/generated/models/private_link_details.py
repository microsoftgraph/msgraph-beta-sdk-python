from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PrivateLinkDetails(AdditionalDataHolder, Parsable):
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
        Instantiates a new privateLinkDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The unique identifier for the Private Link policy.
        self._policy_id: Optional[str] = None
        # The name of the Private Link policy in Azure AD.
        self._policy_name: Optional[str] = None
        # The tenant identifier of the Azure AD tenant the Private Link policy belongs to.
        self._policy_tenant_id: Optional[str] = None
        # The Azure Resource Manager (ARM) path for the Private Link policy resource.
        self._resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivateLinkDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivateLinkDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivateLinkDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policy_id": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policy_name": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "policy_tenant_id": lambda n : setattr(self, 'policy_tenant_id', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
        }
        return fields
    
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
    def policy_id(self,) -> Optional[str]:
        """
        Gets the policyId property value. The unique identifier for the Private Link policy.
        Returns: Optional[str]
        """
        return self._policy_id
    
    @policy_id.setter
    def policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the policyId property value. The unique identifier for the Private Link policy.
        Args:
            value: Value to set for the policyId property.
        """
        self._policy_id = value
    
    @property
    def policy_name(self,) -> Optional[str]:
        """
        Gets the policyName property value. The name of the Private Link policy in Azure AD.
        Returns: Optional[str]
        """
        return self._policy_name
    
    @policy_name.setter
    def policy_name(self,value: Optional[str] = None) -> None:
        """
        Sets the policyName property value. The name of the Private Link policy in Azure AD.
        Args:
            value: Value to set for the policyName property.
        """
        self._policy_name = value
    
    @property
    def policy_tenant_id(self,) -> Optional[str]:
        """
        Gets the policyTenantId property value. The tenant identifier of the Azure AD tenant the Private Link policy belongs to.
        Returns: Optional[str]
        """
        return self._policy_tenant_id
    
    @policy_tenant_id.setter
    def policy_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the policyTenantId property value. The tenant identifier of the Azure AD tenant the Private Link policy belongs to.
        Args:
            value: Value to set for the policyTenantId property.
        """
        self._policy_tenant_id = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. The Azure Resource Manager (ARM) path for the Private Link policy resource.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. The Azure Resource Manager (ARM) path for the Private Link policy resource.
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_str_value("policyTenantId", self.policy_tenant_id)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_additional_data_value(self.additional_data)
    


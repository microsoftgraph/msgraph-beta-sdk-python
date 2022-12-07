from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

tenant_reference = lazy_import('msgraph.generated.models.tenant_reference')

class OutboundSharedUserProfile(AdditionalDataHolder, Parsable):
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
        Instantiates a new outboundSharedUserProfile and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The tenants property
        self._tenants: Optional[List[tenant_reference.TenantReference]] = None
        # The userId property
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutboundSharedUserProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutboundSharedUserProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OutboundSharedUserProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenants": lambda n : setattr(self, 'tenants', n.get_collection_of_object_values(tenant_reference.TenantReference)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("tenants", self.tenants)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenants(self,) -> Optional[List[tenant_reference.TenantReference]]:
        """
        Gets the tenants property value. The tenants property
        Returns: Optional[List[tenant_reference.TenantReference]]
        """
        return self._tenants
    
    @tenants.setter
    def tenants(self,value: Optional[List[tenant_reference.TenantReference]] = None) -> None:
        """
        Sets the tenants property value. The tenants property
        Args:
            value: Value to set for the tenants property.
        """
        self._tenants = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The userId property
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The userId property
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    


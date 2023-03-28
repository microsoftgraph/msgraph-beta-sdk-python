from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import tenant_setup_info

class CompleteSetupPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new completeSetupPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The tenantSetupInfo property
        self._tenant_setup_info: Optional[tenant_setup_info.TenantSetupInfo] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CompleteSetupPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CompleteSetupPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CompleteSetupPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models import tenant_setup_info

        fields: Dict[str, Callable[[Any], None]] = {
            "tenantSetupInfo": lambda n : setattr(self, 'tenant_setup_info', n.get_object_value(tenant_setup_info.TenantSetupInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("tenantSetupInfo", self.tenant_setup_info)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_setup_info(self,) -> Optional[tenant_setup_info.TenantSetupInfo]:
        """
        Gets the tenantSetupInfo property value. The tenantSetupInfo property
        Returns: Optional[tenant_setup_info.TenantSetupInfo]
        """
        return self._tenant_setup_info
    
    @tenant_setup_info.setter
    def tenant_setup_info(self,value: Optional[tenant_setup_info.TenantSetupInfo] = None) -> None:
        """
        Sets the tenantSetupInfo property value. The tenantSetupInfo property
        Args:
            value: Value to set for the tenant_setup_info property.
        """
        self._tenant_setup_info = value
    


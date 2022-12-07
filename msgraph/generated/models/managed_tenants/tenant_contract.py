from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TenantContract(AdditionalDataHolder, Parsable):
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
        Instantiates a new tenantContract and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of relationship that exists between the managing entity and tenant. Optional. Read-only.
        self._contract_type: Optional[int] = None
        # The default domain name for the tenant. Required. Read-only.
        self._default_domain_name: Optional[str] = None
        # The display name for the tenant. Optional. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def contract_type(self,) -> Optional[int]:
        """
        Gets the contractType property value. The type of relationship that exists between the managing entity and tenant. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._contract_type
    
    @contract_type.setter
    def contract_type(self,value: Optional[int] = None) -> None:
        """
        Sets the contractType property value. The type of relationship that exists between the managing entity and tenant. Optional. Read-only.
        Args:
            value: Value to set for the contractType property.
        """
        self._contract_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantContract:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantContract
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantContract()
    
    @property
    def default_domain_name(self,) -> Optional[str]:
        """
        Gets the defaultDomainName property value. The default domain name for the tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._default_domain_name
    
    @default_domain_name.setter
    def default_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultDomainName property value. The default domain name for the tenant. Required. Read-only.
        Args:
            value: Value to set for the defaultDomainName property.
        """
        self._default_domain_name = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the tenant. Optional. Read-only.
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
            "contract_type": lambda n : setattr(self, 'contract_type', n.get_int_value()),
            "default_domain_name": lambda n : setattr(self, 'default_domain_name', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("contractType", self.contract_type)
        writer.write_str_value("defaultDomainName", self.default_domain_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


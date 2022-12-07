from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SpecifiedCaptiveNetworkPlugins(AdditionalDataHolder, Parsable):
    """
    Specifies all the Captive network plugins allowed during the IKEv2 AlwaysOn VPN connection
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
    
    @property
    def allowed_bundle_identifiers(self,) -> Optional[List[str]]:
        """
        Gets the allowedBundleIdentifiers property value. Address of the IKEv2 server. Must be a FQDN, UserFQDN, network address, or ASN1DN
        Returns: Optional[List[str]]
        """
        return self._allowed_bundle_identifiers
    
    @allowed_bundle_identifiers.setter
    def allowed_bundle_identifiers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedBundleIdentifiers property value. Address of the IKEv2 server. Must be a FQDN, UserFQDN, network address, or ASN1DN
        Args:
            value: Value to set for the allowedBundleIdentifiers property.
        """
        self._allowed_bundle_identifiers = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new specifiedCaptiveNetworkPlugins and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Address of the IKEv2 server. Must be a FQDN, UserFQDN, network address, or ASN1DN
        self._allowed_bundle_identifiers: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SpecifiedCaptiveNetworkPlugins:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SpecifiedCaptiveNetworkPlugins
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SpecifiedCaptiveNetworkPlugins()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_bundle_identifiers": lambda n : setattr(self, 'allowed_bundle_identifiers', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("allowedBundleIdentifiers", self.allowed_bundle_identifiers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


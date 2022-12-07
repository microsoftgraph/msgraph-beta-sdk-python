from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class VppTokenLicenseSummary(AdditionalDataHolder, Parsable):
    """
    License summary of a given app in a token.
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
    def apple_id(self,) -> Optional[str]:
        """
        Gets the appleId property value. The Apple Id associated with the given Apple Volume Purchase Program Token.
        Returns: Optional[str]
        """
        return self._apple_id
    
    @apple_id.setter
    def apple_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appleId property value. The Apple Id associated with the given Apple Volume Purchase Program Token.
        Args:
            value: Value to set for the appleId property.
        """
        self._apple_id = value
    
    @property
    def available_license_count(self,) -> Optional[int]:
        """
        Gets the availableLicenseCount property value. The number of VPP licenses available.
        Returns: Optional[int]
        """
        return self._available_license_count
    
    @available_license_count.setter
    def available_license_count(self,value: Optional[int] = None) -> None:
        """
        Sets the availableLicenseCount property value. The number of VPP licenses available.
        Args:
            value: Value to set for the availableLicenseCount property.
        """
        self._available_license_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new vppTokenLicenseSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Apple Id associated with the given Apple Volume Purchase Program Token.
        self._apple_id: Optional[str] = None
        # The number of VPP licenses available.
        self._available_license_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The organization associated with the Apple Volume Purchase Program Token.
        self._organization_name: Optional[str] = None
        # The number of VPP licenses in use.
        self._used_license_count: Optional[int] = None
        # Identifier of the VPP token.
        self._vpp_token_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VppTokenLicenseSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VppTokenLicenseSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VppTokenLicenseSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apple_id": lambda n : setattr(self, 'apple_id', n.get_str_value()),
            "available_license_count": lambda n : setattr(self, 'available_license_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organization_name": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "used_license_count": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
            "vpp_token_id": lambda n : setattr(self, 'vpp_token_id', n.get_str_value()),
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
    def organization_name(self,) -> Optional[str]:
        """
        Gets the organizationName property value. The organization associated with the Apple Volume Purchase Program Token.
        Returns: Optional[str]
        """
        return self._organization_name
    
    @organization_name.setter
    def organization_name(self,value: Optional[str] = None) -> None:
        """
        Sets the organizationName property value. The organization associated with the Apple Volume Purchase Program Token.
        Args:
            value: Value to set for the organizationName property.
        """
        self._organization_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("appleId", self.apple_id)
        writer.write_int_value("availableLicenseCount", self.available_license_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("organizationName", self.organization_name)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
        writer.write_str_value("vppTokenId", self.vpp_token_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def used_license_count(self,) -> Optional[int]:
        """
        Gets the usedLicenseCount property value. The number of VPP licenses in use.
        Returns: Optional[int]
        """
        return self._used_license_count
    
    @used_license_count.setter
    def used_license_count(self,value: Optional[int] = None) -> None:
        """
        Sets the usedLicenseCount property value. The number of VPP licenses in use.
        Args:
            value: Value to set for the usedLicenseCount property.
        """
        self._used_license_count = value
    
    @property
    def vpp_token_id(self,) -> Optional[str]:
        """
        Gets the vppTokenId property value. Identifier of the VPP token.
        Returns: Optional[str]
        """
        return self._vpp_token_id
    
    @vpp_token_id.setter
    def vpp_token_id(self,value: Optional[str] = None) -> None:
        """
        Sets the vppTokenId property value. Identifier of the VPP token.
        Args:
            value: Value to set for the vppTokenId property.
        """
        self._vpp_token_id = value
    


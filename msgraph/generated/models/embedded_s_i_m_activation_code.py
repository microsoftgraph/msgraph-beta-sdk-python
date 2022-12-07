from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class EmbeddedSIMActivationCode(AdditionalDataHolder, Parsable):
    """
    The embedded SIM activation code as provided by the mobile operator.
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
        Instantiates a new embeddedSIMActivationCode and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Integrated Circuit Card Identifier (ICCID) for this embedded SIM activation code as provided by the mobile operator.
        self._integrated_circuit_card_identifier: Optional[str] = None
        # The MatchingIdentifier (MatchingID) as specified in the GSMA Association SGP.22 RSP Technical Specification section 4.1.
        self._matching_identifier: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The fully qualified domain name of the SM-DP+ server as specified in the GSM Association SPG .22 RSP Technical Specification.
        self._smdp_plus_server_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmbeddedSIMActivationCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmbeddedSIMActivationCode
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmbeddedSIMActivationCode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "integrated_circuit_card_identifier": lambda n : setattr(self, 'integrated_circuit_card_identifier', n.get_str_value()),
            "matching_identifier": lambda n : setattr(self, 'matching_identifier', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "smdp_plus_server_address": lambda n : setattr(self, 'smdp_plus_server_address', n.get_str_value()),
        }
        return fields
    
    @property
    def integrated_circuit_card_identifier(self,) -> Optional[str]:
        """
        Gets the integratedCircuitCardIdentifier property value. The Integrated Circuit Card Identifier (ICCID) for this embedded SIM activation code as provided by the mobile operator.
        Returns: Optional[str]
        """
        return self._integrated_circuit_card_identifier
    
    @integrated_circuit_card_identifier.setter
    def integrated_circuit_card_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the integratedCircuitCardIdentifier property value. The Integrated Circuit Card Identifier (ICCID) for this embedded SIM activation code as provided by the mobile operator.
        Args:
            value: Value to set for the integratedCircuitCardIdentifier property.
        """
        self._integrated_circuit_card_identifier = value
    
    @property
    def matching_identifier(self,) -> Optional[str]:
        """
        Gets the matchingIdentifier property value. The MatchingIdentifier (MatchingID) as specified in the GSMA Association SGP.22 RSP Technical Specification section 4.1.
        Returns: Optional[str]
        """
        return self._matching_identifier
    
    @matching_identifier.setter
    def matching_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the matchingIdentifier property value. The MatchingIdentifier (MatchingID) as specified in the GSMA Association SGP.22 RSP Technical Specification section 4.1.
        Args:
            value: Value to set for the matchingIdentifier property.
        """
        self._matching_identifier = value
    
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
        writer.write_str_value("integratedCircuitCardIdentifier", self.integrated_circuit_card_identifier)
        writer.write_str_value("matchingIdentifier", self.matching_identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("smdpPlusServerAddress", self.smdp_plus_server_address)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def smdp_plus_server_address(self,) -> Optional[str]:
        """
        Gets the smdpPlusServerAddress property value. The fully qualified domain name of the SM-DP+ server as specified in the GSM Association SPG .22 RSP Technical Specification.
        Returns: Optional[str]
        """
        return self._smdp_plus_server_address
    
    @smdp_plus_server_address.setter
    def smdp_plus_server_address(self,value: Optional[str] = None) -> None:
        """
        Sets the smdpPlusServerAddress property value. The fully qualified domain name of the SM-DP+ server as specified in the GSM Association SPG .22 RSP Technical Specification.
        Args:
            value: Value to set for the smdpPlusServerAddress property.
        """
        self._smdp_plus_server_address = value
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RankedEmailAddress(AdditionalDataHolder, Parsable):
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
    def address(self,) -> Optional[str]:
        """
        Gets the address property value. The email address.
        Returns: Optional[str]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[str] = None) -> None:
        """
        Sets the address property value. The email address.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new rankedEmailAddress and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The email address.
        self._address: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The rank of the email address. A rank is used as a sort key, in relation to the other returned results. A higher rank value corresponds to a more relevant result. Relevance is determined by communication, collaboration, and business relationship signals.
        self._rank: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RankedEmailAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RankedEmailAddress
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RankedEmailAddress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_float_value()),
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
    def rank(self,) -> Optional[float]:
        """
        Gets the rank property value. The rank of the email address. A rank is used as a sort key, in relation to the other returned results. A higher rank value corresponds to a more relevant result. Relevance is determined by communication, collaboration, and business relationship signals.
        Returns: Optional[float]
        """
        return self._rank
    
    @rank.setter
    def rank(self,value: Optional[float] = None) -> None:
        """
        Sets the rank property value. The rank of the email address. A rank is used as a sort key, in relation to the other returned results. A higher rank value corresponds to a more relevant result. Relevance is determined by communication, collaboration, and business relationship signals.
        Args:
            value: Value to set for the rank property.
        """
        self._rank = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("address", self.address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("rank", self.rank)
        writer.write_additional_data_value(self.additional_data)
    


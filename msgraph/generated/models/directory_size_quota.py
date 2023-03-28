from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class DirectorySizeQuota(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new directorySizeQuota and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Total amount of the directory quota.
        self._total: Optional[int] = None
        # Used amount of the directory quota.
        self._used: Optional[int] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectorySizeQuota:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectorySizeQuota
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DirectorySizeQuota()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
            "used": lambda n : setattr(self, 'used', n.get_int_value()),
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
            value: Value to set for the odata_type property.
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
        writer.write_int_value("total", self.total)
        writer.write_int_value("used", self.used)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total(self,) -> Optional[int]:
        """
        Gets the total property value. Total amount of the directory quota.
        Returns: Optional[int]
        """
        return self._total
    
    @total.setter
    def total(self,value: Optional[int] = None) -> None:
        """
        Sets the total property value. Total amount of the directory quota.
        Args:
            value: Value to set for the total property.
        """
        self._total = value
    
    @property
    def used(self,) -> Optional[int]:
        """
        Gets the used property value. Used amount of the directory quota.
        Returns: Optional[int]
        """
        return self._used
    
    @used.setter
    def used(self,value: Optional[int] = None) -> None:
        """
        Sets the used property value. Used amount of the directory quota.
        Args:
            value: Value to set for the used property.
        """
        self._used = value
    


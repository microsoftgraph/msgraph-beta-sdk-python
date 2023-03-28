from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class OfficeUserCheckinSummary(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new officeUserCheckinSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Total failed user check ins for the last 3 months.
        self._failed_user_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Total successful user check ins for the last 3 months.
        self._succeeded_user_count: Optional[int] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OfficeUserCheckinSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OfficeUserCheckinSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OfficeUserCheckinSummary()
    
    @property
    def failed_user_count(self,) -> Optional[int]:
        """
        Gets the failedUserCount property value. Total failed user check ins for the last 3 months.
        Returns: Optional[int]
        """
        return self._failed_user_count
    
    @failed_user_count.setter
    def failed_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedUserCount property value. Total failed user check ins for the last 3 months.
        Args:
            value: Value to set for the failed_user_count property.
        """
        self._failed_user_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "failedUserCount": lambda n : setattr(self, 'failed_user_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "succeededUserCount": lambda n : setattr(self, 'succeeded_user_count', n.get_int_value()),
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
        writer.write_int_value("failedUserCount", self.failed_user_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("succeededUserCount", self.succeeded_user_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def succeeded_user_count(self,) -> Optional[int]:
        """
        Gets the succeededUserCount property value. Total successful user check ins for the last 3 months.
        Returns: Optional[int]
        """
        return self._succeeded_user_count
    
    @succeeded_user_count.setter
    def succeeded_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the succeededUserCount property value. Total successful user check ins for the last 3 months.
        Args:
            value: Value to set for the succeeded_user_count property.
        """
        self._succeeded_user_count = value
    


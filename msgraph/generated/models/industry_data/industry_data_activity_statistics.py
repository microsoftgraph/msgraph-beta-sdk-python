from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import inbound_activity_results, industry_data_activity_status

class IndustryDataActivityStatistics(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new industryDataActivityStatistics and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identifier for the activity that is being reported on.
        self._activity_id: Optional[str] = None
        # The display name of the underlying flow.
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The status property
        self._status: Optional[industry_data_activity_status.IndustryDataActivityStatus] = None
    
    @property
    def activity_id(self,) -> Optional[str]:
        """
        Gets the activityId property value. The identifier for the activity that is being reported on.
        Returns: Optional[str]
        """
        return self._activity_id
    
    @activity_id.setter
    def activity_id(self,value: Optional[str] = None) -> None:
        """
        Sets the activityId property value. The identifier for the activity that is being reported on.
        Args:
            value: Value to set for the activity_id property.
        """
        self._activity_id = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataActivityStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataActivityStatistics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.industryData.inboundActivityResults":
                from . import inbound_activity_results

                return inbound_activity_results.InboundActivityResults()
        return IndustryDataActivityStatistics()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the underlying flow.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the underlying flow.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import inbound_activity_results, industry_data_activity_status

        fields: Dict[str, Callable[[Any], None]] = {
            "activityId": lambda n : setattr(self, 'activity_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(industry_data_activity_status.IndustryDataActivityStatus)),
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
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[industry_data_activity_status.IndustryDataActivityStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[industry_data_activity_status.IndustryDataActivityStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[industry_data_activity_status.IndustryDataActivityStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

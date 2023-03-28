from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import printer_processing_state, printer_processing_state_detail, printer_processing_state_reason

class PrinterStatus(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new printerStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A human-readable description of the printer's current processing state. Read-only.
        self._description: Optional[str] = None
        # The list of details describing why the printer is in the current state. Valid values are described in the following table. Read-only.
        self._details: Optional[List[printer_processing_state_detail.PrinterProcessingStateDetail]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The processingState property
        self._processing_state: Optional[printer_processing_state.PrinterProcessingState] = None
        # The processingStateDescription property
        self._processing_state_description: Optional[str] = None
        # The processingStateReasons property
        self._processing_state_reasons: Optional[List[printer_processing_state_reason.PrinterProcessingStateReason]] = None
        # The state property
        self._state: Optional[printer_processing_state.PrinterProcessingState] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrinterStatus()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A human-readable description of the printer's current processing state. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A human-readable description of the printer's current processing state. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def details(self,) -> Optional[List[printer_processing_state_detail.PrinterProcessingStateDetail]]:
        """
        Gets the details property value. The list of details describing why the printer is in the current state. Valid values are described in the following table. Read-only.
        Returns: Optional[List[printer_processing_state_detail.PrinterProcessingStateDetail]]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[List[printer_processing_state_detail.PrinterProcessingStateDetail]] = None) -> None:
        """
        Sets the details property value. The list of details describing why the printer is in the current state. Valid values are described in the following table. Read-only.
        Args:
            value: Value to set for the details property.
        """
        self._details = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import printer_processing_state, printer_processing_state_detail, printer_processing_state_reason

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_collection_of_enum_values(printer_processing_state_detail.PrinterProcessingStateDetail)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processingState": lambda n : setattr(self, 'processing_state', n.get_enum_value(printer_processing_state.PrinterProcessingState)),
            "processingStateDescription": lambda n : setattr(self, 'processing_state_description', n.get_str_value()),
            "processingStateReasons": lambda n : setattr(self, 'processing_state_reasons', n.get_collection_of_enum_values(printer_processing_state_reason.PrinterProcessingStateReason)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(printer_processing_state.PrinterProcessingState)),
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
    
    @property
    def processing_state(self,) -> Optional[printer_processing_state.PrinterProcessingState]:
        """
        Gets the processingState property value. The processingState property
        Returns: Optional[printer_processing_state.PrinterProcessingState]
        """
        return self._processing_state
    
    @processing_state.setter
    def processing_state(self,value: Optional[printer_processing_state.PrinterProcessingState] = None) -> None:
        """
        Sets the processingState property value. The processingState property
        Args:
            value: Value to set for the processing_state property.
        """
        self._processing_state = value
    
    @property
    def processing_state_description(self,) -> Optional[str]:
        """
        Gets the processingStateDescription property value. The processingStateDescription property
        Returns: Optional[str]
        """
        return self._processing_state_description
    
    @processing_state_description.setter
    def processing_state_description(self,value: Optional[str] = None) -> None:
        """
        Sets the processingStateDescription property value. The processingStateDescription property
        Args:
            value: Value to set for the processing_state_description property.
        """
        self._processing_state_description = value
    
    @property
    def processing_state_reasons(self,) -> Optional[List[printer_processing_state_reason.PrinterProcessingStateReason]]:
        """
        Gets the processingStateReasons property value. The processingStateReasons property
        Returns: Optional[List[printer_processing_state_reason.PrinterProcessingStateReason]]
        """
        return self._processing_state_reasons
    
    @processing_state_reasons.setter
    def processing_state_reasons(self,value: Optional[List[printer_processing_state_reason.PrinterProcessingStateReason]] = None) -> None:
        """
        Sets the processingStateReasons property value. The processingStateReasons property
        Args:
            value: Value to set for the processing_state_reasons property.
        """
        self._processing_state_reasons = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_enum_value("details", self.details)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("processingState", self.processing_state)
        writer.write_str_value("processingStateDescription", self.processing_state_description)
        writer.write_enum_value("processingStateReasons", self.processing_state_reasons)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[printer_processing_state.PrinterProcessingState]:
        """
        Gets the state property value. The state property
        Returns: Optional[printer_processing_state.PrinterProcessingState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[printer_processing_state.PrinterProcessingState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    


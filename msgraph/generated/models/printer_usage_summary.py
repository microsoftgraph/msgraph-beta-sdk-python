from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')

class PrinterUsageSummary(AdditionalDataHolder, Parsable):
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
    def completed_job_count(self,) -> Optional[int]:
        """
        Gets the completedJobCount property value. The completedJobCount property
        Returns: Optional[int]
        """
        return self._completed_job_count
    
    @completed_job_count.setter
    def completed_job_count(self,value: Optional[int] = None) -> None:
        """
        Sets the completedJobCount property value. The completedJobCount property
        Args:
            value: Value to set for the completedJobCount property.
        """
        self._completed_job_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new printerUsageSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The completedJobCount property
        self._completed_job_count: Optional[int] = None
        # The incompleteJobCount property
        self._incomplete_job_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The printer property
        self._printer: Optional[directory_object.DirectoryObject] = None
        # The printerDisplayName property
        self._printer_display_name: Optional[str] = None
        # The printerId property
        self._printer_id: Optional[str] = None
        # The printerManufacturer property
        self._printer_manufacturer: Optional[str] = None
        # The printerModel property
        self._printer_model: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterUsageSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterUsageSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrinterUsageSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_job_count": lambda n : setattr(self, 'completed_job_count', n.get_int_value()),
            "incomplete_job_count": lambda n : setattr(self, 'incomplete_job_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "printer": lambda n : setattr(self, 'printer', n.get_object_value(directory_object.DirectoryObject)),
            "printer_display_name": lambda n : setattr(self, 'printer_display_name', n.get_str_value()),
            "printer_id": lambda n : setattr(self, 'printer_id', n.get_str_value()),
            "printer_manufacturer": lambda n : setattr(self, 'printer_manufacturer', n.get_str_value()),
            "printer_model": lambda n : setattr(self, 'printer_model', n.get_str_value()),
        }
        return fields
    
    @property
    def incomplete_job_count(self,) -> Optional[int]:
        """
        Gets the incompleteJobCount property value. The incompleteJobCount property
        Returns: Optional[int]
        """
        return self._incomplete_job_count
    
    @incomplete_job_count.setter
    def incomplete_job_count(self,value: Optional[int] = None) -> None:
        """
        Sets the incompleteJobCount property value. The incompleteJobCount property
        Args:
            value: Value to set for the incompleteJobCount property.
        """
        self._incomplete_job_count = value
    
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
    def printer(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the printer property value. The printer property
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._printer
    
    @printer.setter
    def printer(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the printer property value. The printer property
        Args:
            value: Value to set for the printer property.
        """
        self._printer = value
    
    @property
    def printer_display_name(self,) -> Optional[str]:
        """
        Gets the printerDisplayName property value. The printerDisplayName property
        Returns: Optional[str]
        """
        return self._printer_display_name
    
    @printer_display_name.setter
    def printer_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the printerDisplayName property value. The printerDisplayName property
        Args:
            value: Value to set for the printerDisplayName property.
        """
        self._printer_display_name = value
    
    @property
    def printer_id(self,) -> Optional[str]:
        """
        Gets the printerId property value. The printerId property
        Returns: Optional[str]
        """
        return self._printer_id
    
    @printer_id.setter
    def printer_id(self,value: Optional[str] = None) -> None:
        """
        Sets the printerId property value. The printerId property
        Args:
            value: Value to set for the printerId property.
        """
        self._printer_id = value
    
    @property
    def printer_manufacturer(self,) -> Optional[str]:
        """
        Gets the printerManufacturer property value. The printerManufacturer property
        Returns: Optional[str]
        """
        return self._printer_manufacturer
    
    @printer_manufacturer.setter
    def printer_manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the printerManufacturer property value. The printerManufacturer property
        Args:
            value: Value to set for the printerManufacturer property.
        """
        self._printer_manufacturer = value
    
    @property
    def printer_model(self,) -> Optional[str]:
        """
        Gets the printerModel property value. The printerModel property
        Returns: Optional[str]
        """
        return self._printer_model
    
    @printer_model.setter
    def printer_model(self,value: Optional[str] = None) -> None:
        """
        Sets the printerModel property value. The printerModel property
        Args:
            value: Value to set for the printerModel property.
        """
        self._printer_model = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("completedJobCount", self.completed_job_count)
        writer.write_int_value("incompleteJobCount", self.incomplete_job_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("printer", self.printer)
        writer.write_str_value("printerDisplayName", self.printer_display_name)
        writer.write_str_value("printerId", self.printer_id)
        writer.write_str_value("printerManufacturer", self.printer_manufacturer)
        writer.write_str_value("printerModel", self.printer_model)
        writer.write_additional_data_value(self.additional_data)
    


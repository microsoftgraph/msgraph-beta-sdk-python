from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import printer, printer_share, print_connector, print_operation, print_service, print_settings, print_task_definition, report_root

class Print(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new Print and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The list of available print connectors.
        self._connectors: Optional[List[print_connector.PrintConnector]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The operations property
        self._operations: Optional[List[print_operation.PrintOperation]] = None
        # The printerShares property
        self._printer_shares: Optional[List[printer_share.PrinterShare]] = None
        # The list of printers registered in the tenant.
        self._printers: Optional[List[printer.Printer]] = None
        # The reports property
        self._reports: Optional[report_root.ReportRoot] = None
        # The list of available Universal Print service endpoints.
        self._services: Optional[List[print_service.PrintService]] = None
        # Tenant-wide settings for the Universal Print service.
        self._settings: Optional[print_settings.PrintSettings] = None
        # The list of printer shares registered in the tenant.
        self._shares: Optional[List[printer_share.PrinterShare]] = None
        # The taskDefinitions property
        self._task_definitions: Optional[List[print_task_definition.PrintTaskDefinition]] = None
    
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
    def connectors(self,) -> Optional[List[print_connector.PrintConnector]]:
        """
        Gets the connectors property value. The list of available print connectors.
        Returns: Optional[List[print_connector.PrintConnector]]
        """
        return self._connectors
    
    @connectors.setter
    def connectors(self,value: Optional[List[print_connector.PrintConnector]] = None) -> None:
        """
        Sets the connectors property value. The list of available print connectors.
        Args:
            value: Value to set for the connectors property.
        """
        self._connectors = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Print:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Print
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Print()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import printer, printer_share, print_connector, print_operation, print_service, print_settings, print_task_definition, report_root

        fields: Dict[str, Callable[[Any], None]] = {
            "connectors": lambda n : setattr(self, 'connectors', n.get_collection_of_object_values(print_connector.PrintConnector)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(print_operation.PrintOperation)),
            "printers": lambda n : setattr(self, 'printers', n.get_collection_of_object_values(printer.Printer)),
            "printerShares": lambda n : setattr(self, 'printer_shares', n.get_collection_of_object_values(printer_share.PrinterShare)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(report_root.ReportRoot)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(print_service.PrintService)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(print_settings.PrintSettings)),
            "shares": lambda n : setattr(self, 'shares', n.get_collection_of_object_values(printer_share.PrinterShare)),
            "taskDefinitions": lambda n : setattr(self, 'task_definitions', n.get_collection_of_object_values(print_task_definition.PrintTaskDefinition)),
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
    def operations(self,) -> Optional[List[print_operation.PrintOperation]]:
        """
        Gets the operations property value. The operations property
        Returns: Optional[List[print_operation.PrintOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[print_operation.PrintOperation]] = None) -> None:
        """
        Sets the operations property value. The operations property
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def printer_shares(self,) -> Optional[List[printer_share.PrinterShare]]:
        """
        Gets the printerShares property value. The printerShares property
        Returns: Optional[List[printer_share.PrinterShare]]
        """
        return self._printer_shares
    
    @printer_shares.setter
    def printer_shares(self,value: Optional[List[printer_share.PrinterShare]] = None) -> None:
        """
        Sets the printerShares property value. The printerShares property
        Args:
            value: Value to set for the printer_shares property.
        """
        self._printer_shares = value
    
    @property
    def printers(self,) -> Optional[List[printer.Printer]]:
        """
        Gets the printers property value. The list of printers registered in the tenant.
        Returns: Optional[List[printer.Printer]]
        """
        return self._printers
    
    @printers.setter
    def printers(self,value: Optional[List[printer.Printer]] = None) -> None:
        """
        Sets the printers property value. The list of printers registered in the tenant.
        Args:
            value: Value to set for the printers property.
        """
        self._printers = value
    
    @property
    def reports(self,) -> Optional[report_root.ReportRoot]:
        """
        Gets the reports property value. The reports property
        Returns: Optional[report_root.ReportRoot]
        """
        return self._reports
    
    @reports.setter
    def reports(self,value: Optional[report_root.ReportRoot] = None) -> None:
        """
        Sets the reports property value. The reports property
        Args:
            value: Value to set for the reports property.
        """
        self._reports = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("connectors", self.connectors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("printers", self.printers)
        writer.write_collection_of_object_values("printerShares", self.printer_shares)
        writer.write_object_value("reports", self.reports)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("shares", self.shares)
        writer.write_collection_of_object_values("taskDefinitions", self.task_definitions)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def services(self,) -> Optional[List[print_service.PrintService]]:
        """
        Gets the services property value. The list of available Universal Print service endpoints.
        Returns: Optional[List[print_service.PrintService]]
        """
        return self._services
    
    @services.setter
    def services(self,value: Optional[List[print_service.PrintService]] = None) -> None:
        """
        Sets the services property value. The list of available Universal Print service endpoints.
        Args:
            value: Value to set for the services property.
        """
        self._services = value
    
    @property
    def settings(self,) -> Optional[print_settings.PrintSettings]:
        """
        Gets the settings property value. Tenant-wide settings for the Universal Print service.
        Returns: Optional[print_settings.PrintSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[print_settings.PrintSettings] = None) -> None:
        """
        Sets the settings property value. Tenant-wide settings for the Universal Print service.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def shares(self,) -> Optional[List[printer_share.PrinterShare]]:
        """
        Gets the shares property value. The list of printer shares registered in the tenant.
        Returns: Optional[List[printer_share.PrinterShare]]
        """
        return self._shares
    
    @shares.setter
    def shares(self,value: Optional[List[printer_share.PrinterShare]] = None) -> None:
        """
        Sets the shares property value. The list of printer shares registered in the tenant.
        Args:
            value: Value to set for the shares property.
        """
        self._shares = value
    
    @property
    def task_definitions(self,) -> Optional[List[print_task_definition.PrintTaskDefinition]]:
        """
        Gets the taskDefinitions property value. The taskDefinitions property
        Returns: Optional[List[print_task_definition.PrintTaskDefinition]]
        """
        return self._task_definitions
    
    @task_definitions.setter
    def task_definitions(self,value: Optional[List[print_task_definition.PrintTaskDefinition]] = None) -> None:
        """
        Sets the taskDefinitions property value. The taskDefinitions property
        Args:
            value: Value to set for the task_definitions property.
        """
        self._task_definitions = value
    


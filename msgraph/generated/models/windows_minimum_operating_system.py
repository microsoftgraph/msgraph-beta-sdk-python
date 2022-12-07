from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class WindowsMinimumOperatingSystem(AdditionalDataHolder, Parsable):
    """
    The minimum operating system required for a Windows mobile app.
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
        Instantiates a new windowsMinimumOperatingSystem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Windows version 10.0 or later.
        self._v10_0: Optional[bool] = None
        # Windows 10 1607 or later.
        self._v10_1607: Optional[bool] = None
        # Windows 10 1703 or later.
        self._v10_1703: Optional[bool] = None
        # Windows 10 1709 or later.
        self._v10_1709: Optional[bool] = None
        # Windows 10 1803 or later.
        self._v10_1803: Optional[bool] = None
        # Windows 10 1809 or later.
        self._v10_1809: Optional[bool] = None
        # Windows 10 1903 or later.
        self._v10_1903: Optional[bool] = None
        # Windows 10 1909 or later.
        self._v10_1909: Optional[bool] = None
        # Windows 10 2004 or later.
        self._v10_2004: Optional[bool] = None
        # Windows 10 21H1 or later.
        self._v10_21_h1: Optional[bool] = None
        # Windows 10 2H20 or later.
        self._v10_2_h20: Optional[bool] = None
        # Windows version 8.0 or later.
        self._v8_0: Optional[bool] = None
        # Windows version 8.1 or later.
        self._v8_1: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsMinimumOperatingSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsMinimumOperatingSystem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsMinimumOperatingSystem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "v10_0": lambda n : setattr(self, 'v10_0', n.get_bool_value()),
            "v10_1607": lambda n : setattr(self, 'v10_1607', n.get_bool_value()),
            "v10_1703": lambda n : setattr(self, 'v10_1703', n.get_bool_value()),
            "v10_1709": lambda n : setattr(self, 'v10_1709', n.get_bool_value()),
            "v10_1803": lambda n : setattr(self, 'v10_1803', n.get_bool_value()),
            "v10_1809": lambda n : setattr(self, 'v10_1809', n.get_bool_value()),
            "v10_1903": lambda n : setattr(self, 'v10_1903', n.get_bool_value()),
            "v10_1909": lambda n : setattr(self, 'v10_1909', n.get_bool_value()),
            "v10_2004": lambda n : setattr(self, 'v10_2004', n.get_bool_value()),
            "v10_21_h1": lambda n : setattr(self, 'v10_21_h1', n.get_bool_value()),
            "v10_2_h20": lambda n : setattr(self, 'v10_2_h20', n.get_bool_value()),
            "v8_0": lambda n : setattr(self, 'v8_0', n.get_bool_value()),
            "v8_1": lambda n : setattr(self, 'v8_1', n.get_bool_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("v10_0", self.v10_0)
        writer.write_bool_value("v10_1607", self.v10_1607)
        writer.write_bool_value("v10_1703", self.v10_1703)
        writer.write_bool_value("v10_1709", self.v10_1709)
        writer.write_bool_value("v10_1803", self.v10_1803)
        writer.write_bool_value("v10_1809", self.v10_1809)
        writer.write_bool_value("v10_1903", self.v10_1903)
        writer.write_bool_value("v10_1909", self.v10_1909)
        writer.write_bool_value("v10_2004", self.v10_2004)
        writer.write_bool_value("v10_21H1", self.v10_21_h1)
        writer.write_bool_value("v10_2H20", self.v10_2_h20)
        writer.write_bool_value("v8_0", self.v8_0)
        writer.write_bool_value("v8_1", self.v8_1)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def v10_0(self,) -> Optional[bool]:
        """
        Gets the v10_0 property value. Windows version 10.0 or later.
        Returns: Optional[bool]
        """
        return self._v10_0
    
    @v10_0.setter
    def v10_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_0 property value. Windows version 10.0 or later.
        Args:
            value: Value to set for the v10_0 property.
        """
        self._v10_0 = value
    
    @property
    def v10_1607(self,) -> Optional[bool]:
        """
        Gets the v10_1607 property value. Windows 10 1607 or later.
        Returns: Optional[bool]
        """
        return self._v10_1607
    
    @v10_1607.setter
    def v10_1607(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_1607 property value. Windows 10 1607 or later.
        Args:
            value: Value to set for the v10_1607 property.
        """
        self._v10_1607 = value
    
    @property
    def v10_1703(self,) -> Optional[bool]:
        """
        Gets the v10_1703 property value. Windows 10 1703 or later.
        Returns: Optional[bool]
        """
        return self._v10_1703
    
    @v10_1703.setter
    def v10_1703(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_1703 property value. Windows 10 1703 or later.
        Args:
            value: Value to set for the v10_1703 property.
        """
        self._v10_1703 = value
    
    @property
    def v10_1709(self,) -> Optional[bool]:
        """
        Gets the v10_1709 property value. Windows 10 1709 or later.
        Returns: Optional[bool]
        """
        return self._v10_1709
    
    @v10_1709.setter
    def v10_1709(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_1709 property value. Windows 10 1709 or later.
        Args:
            value: Value to set for the v10_1709 property.
        """
        self._v10_1709 = value
    
    @property
    def v10_1803(self,) -> Optional[bool]:
        """
        Gets the v10_1803 property value. Windows 10 1803 or later.
        Returns: Optional[bool]
        """
        return self._v10_1803
    
    @v10_1803.setter
    def v10_1803(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_1803 property value. Windows 10 1803 or later.
        Args:
            value: Value to set for the v10_1803 property.
        """
        self._v10_1803 = value
    
    @property
    def v10_1809(self,) -> Optional[bool]:
        """
        Gets the v10_1809 property value. Windows 10 1809 or later.
        Returns: Optional[bool]
        """
        return self._v10_1809
    
    @v10_1809.setter
    def v10_1809(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_1809 property value. Windows 10 1809 or later.
        Args:
            value: Value to set for the v10_1809 property.
        """
        self._v10_1809 = value
    
    @property
    def v10_1903(self,) -> Optional[bool]:
        """
        Gets the v10_1903 property value. Windows 10 1903 or later.
        Returns: Optional[bool]
        """
        return self._v10_1903
    
    @v10_1903.setter
    def v10_1903(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_1903 property value. Windows 10 1903 or later.
        Args:
            value: Value to set for the v10_1903 property.
        """
        self._v10_1903 = value
    
    @property
    def v10_1909(self,) -> Optional[bool]:
        """
        Gets the v10_1909 property value. Windows 10 1909 or later.
        Returns: Optional[bool]
        """
        return self._v10_1909
    
    @v10_1909.setter
    def v10_1909(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_1909 property value. Windows 10 1909 or later.
        Args:
            value: Value to set for the v10_1909 property.
        """
        self._v10_1909 = value
    
    @property
    def v10_2004(self,) -> Optional[bool]:
        """
        Gets the v10_2004 property value. Windows 10 2004 or later.
        Returns: Optional[bool]
        """
        return self._v10_2004
    
    @v10_2004.setter
    def v10_2004(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_2004 property value. Windows 10 2004 or later.
        Args:
            value: Value to set for the v10_2004 property.
        """
        self._v10_2004 = value
    
    @property
    def v10_21_h1(self,) -> Optional[bool]:
        """
        Gets the v10_21H1 property value. Windows 10 21H1 or later.
        Returns: Optional[bool]
        """
        return self._v10_21_h1
    
    @v10_21_h1.setter
    def v10_21_h1(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_21H1 property value. Windows 10 21H1 or later.
        Args:
            value: Value to set for the v10_21H1 property.
        """
        self._v10_21_h1 = value
    
    @property
    def v10_2_h20(self,) -> Optional[bool]:
        """
        Gets the v10_2H20 property value. Windows 10 2H20 or later.
        Returns: Optional[bool]
        """
        return self._v10_2_h20
    
    @v10_2_h20.setter
    def v10_2_h20(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_2H20 property value. Windows 10 2H20 or later.
        Args:
            value: Value to set for the v10_2H20 property.
        """
        self._v10_2_h20 = value
    
    @property
    def v8_0(self,) -> Optional[bool]:
        """
        Gets the v8_0 property value. Windows version 8.0 or later.
        Returns: Optional[bool]
        """
        return self._v8_0
    
    @v8_0.setter
    def v8_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v8_0 property value. Windows version 8.0 or later.
        Args:
            value: Value to set for the v8_0 property.
        """
        self._v8_0 = value
    
    @property
    def v8_1(self,) -> Optional[bool]:
        """
        Gets the v8_1 property value. Windows version 8.1 or later.
        Returns: Optional[bool]
        """
        return self._v8_1
    
    @v8_1.setter
    def v8_1(self,value: Optional[bool] = None) -> None:
        """
        Sets the v8_1 property value. Windows version 8.1 or later.
        Args:
            value: Value to set for the v8_1 property.
        """
        self._v8_1 = value
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ExcludedApps(AdditionalDataHolder, Parsable):
    """
    Contains properties for Excluded Office365 Apps.
    """
    @property
    def access(self,) -> Optional[bool]:
        """
        Gets the access property value. The value for if MS Office Access should be excluded or not.
        Returns: Optional[bool]
        """
        return self._access
    
    @access.setter
    def access(self,value: Optional[bool] = None) -> None:
        """
        Sets the access property value. The value for if MS Office Access should be excluded or not.
        Args:
            value: Value to set for the access property.
        """
        self._access = value
    
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
    def bing(self,) -> Optional[bool]:
        """
        Gets the bing property value. The value for if Microsoft Search as default should be excluded or not.
        Returns: Optional[bool]
        """
        return self._bing
    
    @bing.setter
    def bing(self,value: Optional[bool] = None) -> None:
        """
        Sets the bing property value. The value for if Microsoft Search as default should be excluded or not.
        Args:
            value: Value to set for the bing property.
        """
        self._bing = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new excludedApps and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The value for if MS Office Access should be excluded or not.
        self._access: Optional[bool] = None
        # The value for if Microsoft Search as default should be excluded or not.
        self._bing: Optional[bool] = None
        # The value for if MS Office Excel should be excluded or not.
        self._excel: Optional[bool] = None
        # The value for if MS Office OneDrive for Business - Groove should be excluded or not.
        self._groove: Optional[bool] = None
        # The value for if MS Office InfoPath should be excluded or not.
        self._info_path: Optional[bool] = None
        # The value for if MS Office Skype for Business - Lync should be excluded or not.
        self._lync: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The value for if MS Office OneDrive should be excluded or not.
        self._one_drive: Optional[bool] = None
        # The value for if MS Office OneNote should be excluded or not.
        self._one_note: Optional[bool] = None
        # The value for if MS Office Outlook should be excluded or not.
        self._outlook: Optional[bool] = None
        # The value for if MS Office PowerPoint should be excluded or not.
        self._power_point: Optional[bool] = None
        # The value for if MS Office Publisher should be excluded or not.
        self._publisher: Optional[bool] = None
        # The value for if MS Office SharePointDesigner should be excluded or not.
        self._share_point_designer: Optional[bool] = None
        # The value for if MS Office Teams should be excluded or not.
        self._teams: Optional[bool] = None
        # The value for if MS Office Visio should be excluded or not.
        self._visio: Optional[bool] = None
        # The value for if MS Office Word should be excluded or not.
        self._word: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExcludedApps:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExcludedApps
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExcludedApps()
    
    @property
    def excel(self,) -> Optional[bool]:
        """
        Gets the excel property value. The value for if MS Office Excel should be excluded or not.
        Returns: Optional[bool]
        """
        return self._excel
    
    @excel.setter
    def excel(self,value: Optional[bool] = None) -> None:
        """
        Sets the excel property value. The value for if MS Office Excel should be excluded or not.
        Args:
            value: Value to set for the excel property.
        """
        self._excel = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access": lambda n : setattr(self, 'access', n.get_bool_value()),
            "bing": lambda n : setattr(self, 'bing', n.get_bool_value()),
            "excel": lambda n : setattr(self, 'excel', n.get_bool_value()),
            "groove": lambda n : setattr(self, 'groove', n.get_bool_value()),
            "info_path": lambda n : setattr(self, 'info_path', n.get_bool_value()),
            "lync": lambda n : setattr(self, 'lync', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "one_drive": lambda n : setattr(self, 'one_drive', n.get_bool_value()),
            "one_note": lambda n : setattr(self, 'one_note', n.get_bool_value()),
            "outlook": lambda n : setattr(self, 'outlook', n.get_bool_value()),
            "power_point": lambda n : setattr(self, 'power_point', n.get_bool_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_bool_value()),
            "share_point_designer": lambda n : setattr(self, 'share_point_designer', n.get_bool_value()),
            "teams": lambda n : setattr(self, 'teams', n.get_bool_value()),
            "visio": lambda n : setattr(self, 'visio', n.get_bool_value()),
            "word": lambda n : setattr(self, 'word', n.get_bool_value()),
        }
        return fields
    
    @property
    def groove(self,) -> Optional[bool]:
        """
        Gets the groove property value. The value for if MS Office OneDrive for Business - Groove should be excluded or not.
        Returns: Optional[bool]
        """
        return self._groove
    
    @groove.setter
    def groove(self,value: Optional[bool] = None) -> None:
        """
        Sets the groove property value. The value for if MS Office OneDrive for Business - Groove should be excluded or not.
        Args:
            value: Value to set for the groove property.
        """
        self._groove = value
    
    @property
    def info_path(self,) -> Optional[bool]:
        """
        Gets the infoPath property value. The value for if MS Office InfoPath should be excluded or not.
        Returns: Optional[bool]
        """
        return self._info_path
    
    @info_path.setter
    def info_path(self,value: Optional[bool] = None) -> None:
        """
        Sets the infoPath property value. The value for if MS Office InfoPath should be excluded or not.
        Args:
            value: Value to set for the infoPath property.
        """
        self._info_path = value
    
    @property
    def lync(self,) -> Optional[bool]:
        """
        Gets the lync property value. The value for if MS Office Skype for Business - Lync should be excluded or not.
        Returns: Optional[bool]
        """
        return self._lync
    
    @lync.setter
    def lync(self,value: Optional[bool] = None) -> None:
        """
        Sets the lync property value. The value for if MS Office Skype for Business - Lync should be excluded or not.
        Args:
            value: Value to set for the lync property.
        """
        self._lync = value
    
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
    def one_drive(self,) -> Optional[bool]:
        """
        Gets the oneDrive property value. The value for if MS Office OneDrive should be excluded or not.
        Returns: Optional[bool]
        """
        return self._one_drive
    
    @one_drive.setter
    def one_drive(self,value: Optional[bool] = None) -> None:
        """
        Sets the oneDrive property value. The value for if MS Office OneDrive should be excluded or not.
        Args:
            value: Value to set for the oneDrive property.
        """
        self._one_drive = value
    
    @property
    def one_note(self,) -> Optional[bool]:
        """
        Gets the oneNote property value. The value for if MS Office OneNote should be excluded or not.
        Returns: Optional[bool]
        """
        return self._one_note
    
    @one_note.setter
    def one_note(self,value: Optional[bool] = None) -> None:
        """
        Sets the oneNote property value. The value for if MS Office OneNote should be excluded or not.
        Args:
            value: Value to set for the oneNote property.
        """
        self._one_note = value
    
    @property
    def outlook(self,) -> Optional[bool]:
        """
        Gets the outlook property value. The value for if MS Office Outlook should be excluded or not.
        Returns: Optional[bool]
        """
        return self._outlook
    
    @outlook.setter
    def outlook(self,value: Optional[bool] = None) -> None:
        """
        Sets the outlook property value. The value for if MS Office Outlook should be excluded or not.
        Args:
            value: Value to set for the outlook property.
        """
        self._outlook = value
    
    @property
    def power_point(self,) -> Optional[bool]:
        """
        Gets the powerPoint property value. The value for if MS Office PowerPoint should be excluded or not.
        Returns: Optional[bool]
        """
        return self._power_point
    
    @power_point.setter
    def power_point(self,value: Optional[bool] = None) -> None:
        """
        Sets the powerPoint property value. The value for if MS Office PowerPoint should be excluded or not.
        Args:
            value: Value to set for the powerPoint property.
        """
        self._power_point = value
    
    @property
    def publisher(self,) -> Optional[bool]:
        """
        Gets the publisher property value. The value for if MS Office Publisher should be excluded or not.
        Returns: Optional[bool]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[bool] = None) -> None:
        """
        Sets the publisher property value. The value for if MS Office Publisher should be excluded or not.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("access", self.access)
        writer.write_bool_value("bing", self.bing)
        writer.write_bool_value("excel", self.excel)
        writer.write_bool_value("groove", self.groove)
        writer.write_bool_value("infoPath", self.info_path)
        writer.write_bool_value("lync", self.lync)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("oneDrive", self.one_drive)
        writer.write_bool_value("oneNote", self.one_note)
        writer.write_bool_value("outlook", self.outlook)
        writer.write_bool_value("powerPoint", self.power_point)
        writer.write_bool_value("publisher", self.publisher)
        writer.write_bool_value("sharePointDesigner", self.share_point_designer)
        writer.write_bool_value("teams", self.teams)
        writer.write_bool_value("visio", self.visio)
        writer.write_bool_value("word", self.word)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def share_point_designer(self,) -> Optional[bool]:
        """
        Gets the sharePointDesigner property value. The value for if MS Office SharePointDesigner should be excluded or not.
        Returns: Optional[bool]
        """
        return self._share_point_designer
    
    @share_point_designer.setter
    def share_point_designer(self,value: Optional[bool] = None) -> None:
        """
        Sets the sharePointDesigner property value. The value for if MS Office SharePointDesigner should be excluded or not.
        Args:
            value: Value to set for the sharePointDesigner property.
        """
        self._share_point_designer = value
    
    @property
    def teams(self,) -> Optional[bool]:
        """
        Gets the teams property value. The value for if MS Office Teams should be excluded or not.
        Returns: Optional[bool]
        """
        return self._teams
    
    @teams.setter
    def teams(self,value: Optional[bool] = None) -> None:
        """
        Sets the teams property value. The value for if MS Office Teams should be excluded or not.
        Args:
            value: Value to set for the teams property.
        """
        self._teams = value
    
    @property
    def visio(self,) -> Optional[bool]:
        """
        Gets the visio property value. The value for if MS Office Visio should be excluded or not.
        Returns: Optional[bool]
        """
        return self._visio
    
    @visio.setter
    def visio(self,value: Optional[bool] = None) -> None:
        """
        Sets the visio property value. The value for if MS Office Visio should be excluded or not.
        Args:
            value: Value to set for the visio property.
        """
        self._visio = value
    
    @property
    def word(self,) -> Optional[bool]:
        """
        Gets the word property value. The value for if MS Office Word should be excluded or not.
        Returns: Optional[bool]
        """
        return self._word
    
    @word.setter
    def word(self,value: Optional[bool] = None) -> None:
        """
        Sets the word property value. The value for if MS Office Word should be excluded or not.
        Args:
            value: Value to set for the word property.
        """
        self._word = value
    

